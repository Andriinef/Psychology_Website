from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from blog.forms import UserCreationForm
from blog.models import Clients

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    add_form = UserCreationForm

@admin.register(Clients)
class Client(admin.ModelAdmin):
    list_display = [
        "date_created",
        "username",
        "slug",
        "phone",
        "question",
    ]

    prepopulated_fields = {"slug": ("username",)}
    search_fields = ("date_created", 'username', 'question')
