from django.contrib import admin

from .models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_admin', 'is_active', 'last_login']
    list_editable = ['is_admin', 'is_active']
    list_filter = ['email', 'is_admin', 'is_active', 'last_login']
