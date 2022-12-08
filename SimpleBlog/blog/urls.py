"""SimpleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    # path('', RedirectView.as_view(url='/blog/', permanent=True)),
    path('', views.index, name='index'),
    path('blog/', views.PostsListView.as_view(), name='blog'),
    path('blog', views.PostsListView.as_view(), name='blog'),
    path('blog/<int:pk>/', views.PostDetailView.as_view()),
    path('blog/<int:pk>', views.PostDetailView.as_view()),
    path('blog/create_post/', views.CreatePost.as_view()),
    path('signup/', views.SignUpView.as_view(), name="signup"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
