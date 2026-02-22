from django.shortcuts import render, get_object_or_404
from .models import Project


def projects(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects':projects})



def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def profile(request):
    return render(request, 'profile.html')
