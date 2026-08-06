from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.personal_info_view, name='personal_info'),
    path('projects/', views.list_view, name='project_list'),
    path('projects/<int:pk>/', views.detail_view, name='project_detail'),
]