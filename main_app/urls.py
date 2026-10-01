from django.urls import path
from . import views

urlpatterns = [
    # The home page root URL
    path('', views.personal_info_view, name='home'),
    
    # About and Projects
    path('about/', views.personal_info_view, name='personal_info'),
    path('projects/', views.list_view, name='project_list'),
    path('projects/<int:pk>/', views.detail_view, name='project_detail'),
    path('projects/add/', views.project_create_view, name='project_create'),
    
    # Contact and Testimonies
    path('contact/', views.contact_view, name='contact'),
    path('testimonies/add/', views.testimony_create_view, name='testimony_create'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/<int:pk>/', views.testimony_detail_view, name='testimony_detail'),
]