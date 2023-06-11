
from django import forms
from blog.models import Comment, Blog

# Create your forms here.
class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ('blog_title', 'blog_text', 'blog_image', 'writer_name', 'blog_category')
        # exclude = ("comment",)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ('your_comment',)
        fields = ('name', 'email', 'your_comment')
        # widgets = {'blog': forms.HiddenInput()}

# class ReactionForm(forms.ModelForm):
#     reaction = forms.ChoiceField(choices=Comment.your_reaction)

#     class Meta:
#         model = Comment
#         fields = ('reaction',)
