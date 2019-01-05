from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html',{'blogs':blogs})

def detail(request, blog_id):
    # blogs = Blog.objects
    # x = []
    # for b in blogs.all():
    #     x.append(b.id)
    #
    # y = x[blog_id-1]
    # detailblog = get_object_or_404(Blog, pk=y)
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':detailblog})
