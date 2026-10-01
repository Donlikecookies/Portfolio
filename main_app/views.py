from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import PersonalInformation, Project, Testimony, Inquiry
from .forms import ProjectForm, TestimonyForm
from django.contrib import messages

def personal_info_view(request):
    info = PersonalInformation.objects.first()
    return render(request, 'main_app/personal_info.html', {'info': info})

def list_view(request):
    projects = Project.objects.all()
    return render(request, 'main_app/project_list.html', {'projects': projects})

def detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main_app/project_detail.html', {'project': project})

def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success! Your new project has been added.")
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'main_app/project_form.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            message=request.POST.get('message')
        )
        messages.success(request, "Thank you! Your inquiry has been sent.")
        return redirect('contact') # Redirect to prevent duplicate submissions
    return render(request, 'main_app/contact.html')

def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success! Your new project has been added.")
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'main_app/project_form.html', {'form': form})


# 3b. List Testimonies: CLASS-BASED LIST VIEW (CBV)
class TestimonyListView(ListView):
    model = Testimony
    template_name = 'main_app/testimony_list.html'
    context_object_name = 'testimonies'


# 3c. Detail Testimony: FUNCTION-BASED DETAIL VIEW (FBV)
def testimony_detail_view(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'main_app/testimony_detail.html', {'testimony': testimony})