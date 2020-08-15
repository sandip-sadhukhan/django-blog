from django.shortcuts import render, redirect
from .models import BlogPost

def home(request):
    blogs = BlogPost.objects.all()

    return render(request, 'home.html', {'blogs':blogs})


def blog(request, pk):
    blog = BlogPost.objects.get(pk=pk)

    return render(request, 'blog/blog.html', {'blog': blog})

def create_blog(request):

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        content = request.POST['content']
        newBlog = BlogPost()
        newBlog.title = title
        newBlog.description = description
        newBlog.content = content
        newBlog.save()
        return redirect('/')

    return render(request, 'blog/createblog.html')