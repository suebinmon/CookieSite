import re
from django.db import models
from django.utils import timezone
from django.conf import settings
from django import forms
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title = models.CharField(max_length=100)
	content = models.TextField(null=True, blank=True)
	photo = models.ImageField(upload_to='%Y/%m/%d/orig', blank=True, null=True)
	is_public = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-created_at']

	def get_absolute_url(self):
		return reverse('board:post_detail', args=[self.pk])

	#def delete(self, *args, **kwargs):
		#self.image.delete()
		#super(Post, self).delete(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_edit_url(self):
		return reverse('board:post_edit', args=[self.pk])

	def get_delete_url(self):
		return reverse('board:post_delete', args=[self.pk])

class Comment(models.Model):
	#Post:Comment = 1:N
	post = models.ForeignKey(Post)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	is_public = models.BooleanField(default=False)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.message

	def get_edit_url(self):
		return reverse('board:comment_edit', args=[self.post.pk, self.pk])

	def get_delete_url(self):
		return reverse('board:comment_delete', args=[self.post.pk, self.pk])