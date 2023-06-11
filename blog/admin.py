from django.contrib import admin
from blog.models import Comment, Writer, Blog, Category
# Register your models here.

admin.site.register(Blog)
admin.site.register(Writer)
# admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'your_comment', 'created_on', 'active', 'blog')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'your_comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Category)
