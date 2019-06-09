from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
	blogs = Blog.objects
	return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_title):
	detailblog = get_object_or_404(Blog, slug=blog_title)
	return render(request, 'blog/detail.html', {'detailblog': detailblog})
