from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta():
		model = Post
		fields = ['title', 'content', 'author']

class UserSerializer(serializers.ModelSerializer):
	class Meta():
		model = User
		fields = ['username', 'password']