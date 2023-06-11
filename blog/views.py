# import copy

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.http import request
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic.base import View
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator

from blog.models import Blog, Writer, Comment, Category
from blog.serializers import BlogSerializer, WriterSerializer
from blog.forms import CommentForm, BlogForm
# from accounts.models import Users


def bloghome(request):

    if request.method == 'GET':
        blogs = Blog.objects.all()
        categories = Category.objects.all()
        category_id = request.GET.get('category')

        if category_id:
            blogs = Blog.get_blogs_by_category_id(category_id=category_id).order_by('blog_date_time')
        else:
            blogs = Blog.objects.all().order_by('blog_date_time')

        paginator = Paginator(blogs, per_page=2)  # Show 1 contact per page.
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
        # if category_id:
        #     page_obj = page_obj.object_list.filter(category_id=category_id)
        # else:
        #     page_obj = page_obj

    return render(request, 'blog/blog.html', {'page_obj':page_obj, 'categories':categories})
    # return render(request, 'blog/blog.html', {'blogs':blogs, 'categories':categories})

# class BlogFormView(View):

#     def get(self, request):

#         blog_form = BlogForm()
#         return render(request, 'blog/blog-form.html', {'blog_form':blog_form})

#     def post(self, request):
#         return BlogFormView.if_post(request)

#     def if_post(request):
#         blog_form = BlogFormView(request.POST)#, request.FILES

#         if blog_form.is_valid():
#             blog_form.save()
#             messages.success(request, ('Your blog was successfully added!'))
#         else:
#             messages.error(request, 'Error saving form')

#         # return bloghome(request)
#         return render('blog/blog.html')


# Blog-form-view
def BlogFormView(request):

    blog_form = BlogForm()

    if request.method == "POST":
        blog_form = BlogForm(request.POST, request.FILES)

        if blog_form.is_valid():
            blog_form.save()

            messages.success(request, ('Your blog was successfully added!'))
        else:
            messages.error(request, 'Error saving form')

        return redirect('blog')

    return render(request=request, template_name="blog/blog-form.html", context={'blog_form':blog_form})

class BlogView(View):

    def get(self,request,pk):

        blog = Blog.objects.get(id=pk)
        comment_form = CommentForm()
        comments = Comment.objects.filter(blog = blog.id)
        categories = Category.objects.all()
        category_id = request.GET.get('category')

        if category_id:
            blogs = Blog.get_blogs_by_category_id(category_id=category_id)
            return render(request, 'blog/blog.html', {'blogs':blogs, 'categories':categories})
        else:
            return render(request,'blog/blog-view.html', {'blog':blog, 'comment_form':comment_form, 'comments':comments, 'categories':categories})

    def post(self,request,pk):

        blog = Blog.objects.get(id=pk)
        comment_form = CommentForm(data=request.POST)
        # form_data = copy.copy(request.POST)
        # form_data['blog'] = blog.id
        # comment_form = CommentForm(data=form_data)

        if comment_form.is_valid:
            blog_id = blog.id
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog_id
            new_comment.save()
            # comment_form.save()

        # messages.success(request, ('Your comment was added successfully!'))
        return redirect('blog')
        # return render(request, 'blog/blog-view.html', {'comment_form':comment_form})

# class BlogSearchResult(ListView):
#     model = Blog
#     template_name = 'blog/search-view.html'
#     # queryset = Blog.objects.filter(blog_title__icontains="Javascript")

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         q = self.request.GET.get("query")
#         # q = self.kwargs.get('query')
#         if q:
#             queryset = queryset.filter(
#                 Q(blog_title__icontains=q) |
#                 Q(blog_text__icontains=q)
#                 ).distinct()
#             return queryset
#         else:
#             return queryset.none()


class BlogSearchView(ListView):
    model = Blog
    template_name = 'blog/search-view.html'
    context_object_name = 'blogs'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            queryset = Blog.objects.filter(
                Q(blog_title__icontains=query) |
                Q(blog_text__icontains=query)
            ).distinct()
            return queryset
        else:
            return Blog.objects.none()


# class PaginatedListView(ListView):
#     paginate_by = 1
#     model = Blog

# def pagination_view(request):
#     blogs = Blog.objects.all().order_by("blog_date_time")
#     paginator = Paginator(blogs, per_page=1)  # Show 1 contact per page.

#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, "blog/blog.html", {"page_obj": page_obj})


# def create_superuser(self, email, password):
#         """
#         Create and return a `User` with superuser (admin) permissions.
#         """
#         if password is None:
#             raise TypeError('Superusers must have a password.')

#         user = self.create_user(email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()

#         return user

class BlogAV(APIView):

    def get(self, request):

        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailAV(APIView):

    def get(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({'error':'Not found'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = Blog(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        # return Response({'message':'this data is deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)


class WriterAV(APIView):

    def get(self, request):
        writer = Writer.objects.all()
        serializer = WriterSerializer(writer, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = WriterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
