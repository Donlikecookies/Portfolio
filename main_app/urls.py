from django.urls import path
from . import views

urlpatterns = [
    # Replace 'home' with whatever function name you created in views.py
    path('', views.home, name='home'), 
]