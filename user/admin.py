from django.contrib import admin
from user.models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'phone', 'city','state','country']
admin.site.register(UserProfile, UserProfileAdmin)