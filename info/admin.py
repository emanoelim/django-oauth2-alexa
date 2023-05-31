from django.contrib import admin

from info.models import Info


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('info',)
