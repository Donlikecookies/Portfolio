from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required

from .models import PersonalInformation, Project, Testimony, Inquiry, TechStack
from .forms import ProjectForm, TestimonyForm, TechStackForm

# ==========================================
# PUBLIC PORTFOLIO VIEWS (Quiz 1 - 3)
# ==========================================

def personal_info_view(request):
    info = PersonalInformation.objects.first()
    return render(request, 'main_app/personal_info.html', {'info': info})

def list_view(request):
    projects = Project.objects.all()
    return render(request, 'main_app/project_list.html', {'projects': projects})

def detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main_app/project_detail.html', {'project': project})

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
        return redirect('contact')
    return render(request, 'main_app/contact.html')

def testimony_create_view(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your testimony has been submitted.")
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    return render(request, 'main_app/testimony_form.html', {'form': form})

class TestimonyListView(ListView):
    model = Testimony
    template_name = 'main_app/testimony_list.html'
    context_object_name = 'testimonies'

def testimony_detail_view(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'main_app/testimony_detail.html', {'testimony': testimony})


def admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Only admin users are allowed.")
    else:
        form = AuthenticationForm()
    return render(request, 'main_app/admin_login.html', {'form': form})

@staff_member_required
def dashboard_view(request):
    projects = Project.objects.all()
    tech_stacks = TechStack.objects.all()
    return render(request, 'main_app/dashboard.html', {
        'projects': projects,
        'tech_stacks': tech_stacks
    })

@staff_member_required
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success! Your new project has been added.")
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'main_app/project_form.html', {'form': form})

@staff_member_required
def add_tech_stack_view(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tech Stack Added!")
            return redirect('dashboard')
    else:
        form = TechStackForm()
    return render(request, 'main_app/add_tech_stack.html', {'form': form})

@staff_member_required
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success! Your new project has been added.")
            return redirect('dashboard')
        else:
            # Print form errors to your VS Code terminal to see what's failing
            print(form.errors)
    else:
        form = ProjectForm()
    return render(request, 'main_app/project_form.html', {'form': form})