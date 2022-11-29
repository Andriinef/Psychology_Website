from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from blog.forms import UserCreationForm
from blog.models import Clients, Status

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    add_form = UserCreationForm


@admin.register(Clients)
class Client(admin.ModelAdmin):
    list_display = [
        "id",
        "date_created",
        "username",
        "phone",
        "question",
        "status",
    ]

    search_fields = ("date_created", "username", "question", "phone",)


@admin.register(Status)
class Status(admin.ModelAdmin):
    list_display = ["id", "status_question", ]
    search_fields = ("id", "status_question",)
