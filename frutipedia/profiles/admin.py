from django.contrib import admin

from frutipedia.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "age")
