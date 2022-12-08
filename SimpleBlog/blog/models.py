from datetime import datetime as dt
from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255) # заголовок поста
	datetime = models.DateTimeField(u'Дата публикации', auto_now_add=True) # дата публикации
	content = models.TextField(max_length=10000) # текст поста
	author = models.CharField(max_length=64, ) # автор
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return "/blog/%i/" % self.id


class New(models.Model):
	title = models.CharField(max_length=255) # заголовок новости
	datetime = models.DateTimeField(u'Дата публикации', auto_now_add=True) # дата публикации
	content = models.TextField(max_length=10000) # текст новости
	author = models.CharField(max_length=64, ) # автор
	
	def __unicode__(self):
		return self.title
