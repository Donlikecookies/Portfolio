from django.shortcuts import render, get_object_or_404
from .models import PersonalInformation, Project

def personal_info_view(request):
    info = PersonalInformation.objects.first()
    return render(request, 'main_app/personal_info.html', {'info': info})

def list_view(request):
    projects = Project.objects.all()
    return render(request, 'main_app/project_list.html', {'projects': projects})

def detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main_app/project_detail.html', {'project': project})