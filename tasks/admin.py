from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('user','title', 'description', 'is_completed', 'priority')
    readonly_fields = ('user',)

    list_display = ('title', 'is_completed', 'created_at', 'updated_at', 'priority')
    list_filter = ('is_completed', 'created_at', 'priority')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_display_links = ('title',)
    list_editable = ('is_completed', 'priority')

