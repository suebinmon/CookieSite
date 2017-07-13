from django.contrib import admin
from .models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'is_public', 'created_at']
	list_display_links = ['title']
	list_editable = ['is_public']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'message', 'is_public', 'created_at']
	list_display_links = ['message']
	list_editable = ['is_public']

