from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# ----- User ----- #

class User(AbstractUser):
    """ Model: User(Memories author) """

    avatar = models.URLField(
        verbose_name=_("Автар пользователя"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
