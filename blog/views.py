from django.shortcuts import render

from blog.models import BlogPost


# Create your views here.

def blog(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'blog/blog.html', {'posts': posts, 'request': request})