from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class Status(models.Model):
    status_question = models.CharField("Стан питання", max_length=30,)

    class Meta:
        verbose_name = "Стан питання"
        verbose_name_plural = "Стан питань"

    def __str__(self):
        return self.status_question

    def det_absolute_url(self):
        return reverse("status_question", kwargs={"status_question": self.id})


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Clients(models.Model):
    username = models.CharField("Кліент", max_length=150,)
    phone = models.CharField(max_length=16, blank=True, null=True,)
    question = models.TextField(
        "Текст питання", max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.ForeignKey("Status", on_delete=models.PROTECT, default=1,
                               max_length=30, verbose_name="Стан питання")

    class Meta:
        verbose_name = "Кліент"
        verbose_name_plural = "Кліенти"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("username", kwargs={"username": self.id})
