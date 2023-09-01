from django.shortcuts import render, redirect
from .models import Post

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist': postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post': post})

def new_post(request):
    if request.method == 'POST':
        postname = request.POST.get('postname')
        contents = request.POST.get('contents')
        new_post = Post(postname=postname, contents=contents)
        new_post.save()
        return redirect('/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'main/remove_post.html', {'Post': post})


def index(request):
    return redirect("/")