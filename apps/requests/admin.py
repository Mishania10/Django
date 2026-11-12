from django.contrib import admin

from .models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'category', 'priority', 'status', 'assignee', 'created_at')
    list_filter = ('status', 'category', 'priority', 'created_at')
    search_fields = ('title', 'name', 'email', 'description')
    list_editable = ('status', 'assignee')
    readonly_fields = ('created_at', 'updated_at')
