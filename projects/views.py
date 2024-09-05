from django.shortcuts import render
from .models import Project
# Create your views here.


def projects(request):
    projects = Project.objects.order_by('-display_date')
    return render(request, 'projects/projects.html', {'request': request, 'projects': projects})
