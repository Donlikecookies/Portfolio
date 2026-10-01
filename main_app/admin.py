from django.contrib import admin
from .models import PersonalInformation, Project, Testimony, Inquiry, TechStack

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # We use a custom method 'get_tech_stacks' to display them as a comma-separated list
    list_display = ('project_name', 'get_tech_stacks')

    def get_tech_stacks(self, obj):
        return ", ".join([t.name for t in obj.tech_stacks.all()])
    get_tech_stacks.short_description = 'Tech Stacks'

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'content')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(PersonalInformation)
admin.site.register(TechStack)