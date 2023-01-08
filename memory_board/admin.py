from django.contrib import admin

from .models import MemoryPlacesModel


# ----- MemoryPlacesModelAdmin ----- #

@admin.register(MemoryPlacesModel)
class MemoryPlacesAdmin(admin.ModelAdmin):
    """ Register Amdin for model MemoryPlacesModel"""

    # Settings slug for create new memories:
    prepopulated_fields = {"slug": ("title",), }
