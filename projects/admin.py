from django.contrib import admin

from projects.models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link')
    fields = ('title', 'display_date', 'github_link', 'description',)


admin.site.register(Project, ProjectAdmin)