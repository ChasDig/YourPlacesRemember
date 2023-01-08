from django.db import models

from django.conf import settings
from django.urls import reverse

from slugify import slugify

from accounts.models import User


# ----- Models: Memory ----- #

class MemoryPlacesModel(models.Model):
    """ Model: Memory about places """

    title = models.CharField(
        verbose_name="Название места",
        max_length=128,
    )

    description = models.TextField(
        verbose_name="Описание места",
        max_length=2048,
        blank=True,
    )

    review = models.TextField(
        verbose_name="Воспоминание о месте",
        max_length=2048,
    )

    address = models.CharField(
        verbose_name="Адрес места",
        max_length=128,
    )

    data_published_memory = models.DateTimeField(
        verbose_name="Дата и время создания воспоминания",
        auto_now_add=True,
    )

    user = models.ForeignKey(
        verbose_name="Автор воспоминания",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='memory_list',
        blank=True,
        null=True,
    )

    images = models.ImageField(
        verbose_name="Фотографии с впечатлениями",
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        verbose_name="Slug воспоминания",
        max_length=128,
        unique=True,
        db_index=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("memory_detail", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(MemoryPlacesModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Воспоминание"
        verbose_name_plural = "Воспоминания"
        ordering = ["-data_published_memory"]
