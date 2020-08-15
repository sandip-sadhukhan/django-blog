from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<str:pk>/', views.blog, name="blog"),
    path('create_blog/', views.create_blog, name="create_blog"),
]
