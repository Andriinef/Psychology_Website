from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# class Role(models.TextChoices):
#     """Роли пользователей"""

#     ASISTENT = 'ASISTENT', 'Помощник'


class User(AbstractUser):
    pass
    # role = models.CharField(
    #     max_length=15,
    #     choices=Role.choices,
    #     default=Role.ASISTENT
    # )
    # email = models.EmailField(
    #     _('email address'),
    #     unique=True,
    # )

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
