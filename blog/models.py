from django.db import models
from datetime import datetime
# Create your models here.

# from django.conf import settings
# from django.contrib.auth import get_user_model
from django.db import models
                                                                                                                                                                
# UserModel = get_user_model()

# class Profile(models.Model):
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

class Writer(models.Model):
    writer_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.writer_name


class Category(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic
    
    # @classmethod
    # def get_default_pk(cls):
    #     category, id = cls.objects.get_or_create(
    #         topic='python', id = 1)
    #     return category.pk


class Blog(models.Model):

    blog_title = models.CharField(default="Title", max_length=100)
    blog_text = models.TextField(default="My Blog", max_length=10000)
    blog_image = models.ImageField(upload_to="images/blog")
    blog_date_time = models.DateTimeField(default=datetime.now)
    writer_name = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name = 'writer')
       
    # blog_category = models.OneToOneField(Category, on_delete=models.CASCADE, default=0, related_name = "category") #default=Category.get_default_pk, related_name = "category")
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # writer_name = models.CharField(default='writer', max_length=50)
    # models.OneToOneField(UserModel, on_delete=models.CASCADE)
    # comment = models.ForeignKey(Comment, related_name='comment', on_delete=models.CASCADE, default="no comments", blank=True)

    def all_blogs():
        return Blog.objects.all()

    def __str__(self):
        return self.blog_title

    def get_blogs_by_category_id(category_id):
        return Blog.objects.filter(blog_category_id=category_id)

class Comment(models.Model):
    # your_comment = models.CharField(max_length = 500, blank=True)
    # reaction = :
    name = models.CharField(max_length=80, default='name', blank=True)
    email = models.EmailField(default="email", blank=True)
    # your_comment = models.TextField(blank=True)
    your_comment = models.CharField(max_length=500, default="your comment", blank=True)
    created_on = models.DateTimeField(default=datetime.now)#auto_now_add=True)
    active = models.BooleanField(default=False)
    # blog = models.ForeignKey(Blog, on_delete=models.CASCADE) #default=1, blank=True)
    blog = models.IntegerField(blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.your_comment, self.name)

    # def get_all_blogs_by_category_id(cate)

# JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies
# of the World Wide Web, alongside HTML and CSS. As of 2022, 98% of websites use JavaScript on the
# client side for webpage behavior, often incorporating third-party libraries.
# JavaScript is a scripting language that enables you to create dynamically updating content, control
# multimedia, animate images, and pretty much everything else.

# Common uses for JavaScript are image manipulation, form validation, and dynamic changes of content.
# To select an HTML element, JavaScript most often uses the document.getElementById() method.

# Running the Python backend with JavaScript frontend:
# Make sure the backend server is running by running the command python app.py in the terminal/command
# prompt in the backend directory. Then start the frontend web server if it is not running in the frontend directory: http-server .

# Python is a high-level, general-purpose programming language.
# Its design philosophy emphasizes code readability with the use of
# significant indentation via the off-side rule.
# Python is dynamically typed and garbage-collected.
# Python can be used on a server to create web applications. 
# Python is a computer programming language often used to build
# websites and software, automate tasks, and conduct data analysis.
# Python is a general-purpose language, meaning it can be used to
# create a variety of different programs and isn't specialized for any specific problems.