from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from blog.models import Clients, Status

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=50,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
        help_text="Наприклад: admin@gmail.com",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class RecordingQuestionFofm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Clients
        fields = [
            "username",
            "phone",
            "question",
        ]


class UpdateStatusQuestionFofm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Clients
        fields = [
            "status",
        ]
