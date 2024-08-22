from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'mySite/index.html', {'request': request})


def about(request):
    return render(request, 'mySite/about.html', {'request': request})

def experience(request):
    return render(request, 'mySite/experience.html', {'request': request})


def projects(request):
    return render(request, 'mySite/projects.html', {'request': request})


def blog(request):
    return render(request, 'mySite/blog.html', {'request': request})


def contact(request):
    return render(request, 'mySite/contact.html', {'request': request})
