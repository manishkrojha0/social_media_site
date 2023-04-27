from django.contrib import admin
from core.models.profiles import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile