# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from blog.models import Blog, Writer

class BlogSerializer(serializers.ModelSerializer):
    # blog_cover = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Blog
        fields = "__all__"
        
class WriterSerializer(serializers.ModelSerializer):
    writer_name = serializers.StringRelatedField(read_only=True)
    # myblogs = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Writer
        fields = ('writer_name',)
