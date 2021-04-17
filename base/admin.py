from django.contrib.admin import ModelAdmin, site
from .models import User


class UserAdmin(ModelAdmin):
    list_display = ['pk', 'username', 'first_name', 'last_name', 'email']


site.register(User, UserAdmin)

