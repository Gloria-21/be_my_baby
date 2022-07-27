from django.shortcuts import render, redirect, reverse

from .models import Post


def blog(request):
    posts = Post.objects.all()
    template = 'blog/blog.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)

