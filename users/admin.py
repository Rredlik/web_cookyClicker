from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import Task, Core

User = get_user_model()

admin.site.register(Task)
admin.site.register(Core)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
