from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_es', 'description', 'description_es', 'technology','slug', 'image', 'link')

admin.site.register(Project, ProjectAdmin)

# Register your models here.
