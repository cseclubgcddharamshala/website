from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'created_at', 'is_active')
    list_filter = ('priority', 'is_active')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
