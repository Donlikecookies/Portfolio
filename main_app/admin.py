from django.contrib import admin
from .models import PersonalInformation, Project, Testimony, Inquiry

# Adding list_display makes the admin table much easier to read
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'tech_stack')

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'content')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(PersonalInformation)