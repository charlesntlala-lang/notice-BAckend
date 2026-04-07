from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'content']
