from django.contrib import admin
from projects.models import Project, Task, Counter

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date')
    search_fields = ('name',)
    raw_id_fields = ('project',)

class ProjectAdmin(admin.ModelAdmin):		
	list_display = ('name', 'start_date')
	ordering = ('start_date',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Counter)