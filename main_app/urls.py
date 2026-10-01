from django.urls import path
from . import views

urlpatterns = [
    # Public Pages
    path('', views.personal_info_view, name='home'),
    path('about/', views.personal_info_view, name='personal_info'),
    path('projects/', views.list_view, name='project_list'),
    path('projects/<int:pk>/', views.detail_view, name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('testimonies/add/', views.testimony_create_view, name='testimony_create'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/<int:pk>/', views.testimony_detail_view, name='testimony_detail'),
    
    # Quiz 5 & 6: Admin & Dashboard Pages
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/projects/add/', views.project_create_view, name='project_create'),
    path('dashboard/tech-stacks/add/', views.add_tech_stack_view, name='add_tech_stack'),
]