import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Clients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        "Кліент",
        max_length=150,
    )
    # slug = models.SlugField(max_length=150, unique=True, verbose_name="URL")
    # phone = PhoneNumberField(blank=True, help_text='Контактний телефон')
    phone = models.TextField("Телефон", max_length=250, blank=True, null=True)
    question = models.TextField("Текст питання", max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Кліент"
        verbose_name_plural = "Кліенти"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("username", kwargs={"id": self.id})
