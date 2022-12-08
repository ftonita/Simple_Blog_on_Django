from datetime import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from rest_framework.decorators import APIView
from django.contrib.auth.decorators import login_required
from blog.models import Post as Ps, New
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from blog.serializers import PostSerializer
# Create your views here.

class PostsListView(ListView): # представление в виде списка
    model = Ps                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Ps

class CreatePost(APIView):
    user = User()
    @login_required
    def post(self, request):
        print(request.POST)
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect('/blog/')
        return HttpResponseRedirect(error_page)

def index(request):
    # request.session.user = request.user
    # print(request.session.get('user'))
    news = New.objects.all()
    return render(request, 'blog/index.html', status=200, context={"object_list": news})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def error_page(request, exception):
    return render(request, 'blog/error.html', status=400)

def server_error(request):
    return render(request, 'blog/error.html', status=400)