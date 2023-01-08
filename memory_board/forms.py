from django import forms

from .models import MemoryPlacesModel


# ----- Places Memory forms ----- #

class MemoryCreateForm(forms.ModelForm):
    """ Forms: Create remember Form """

    class Meta:

        model = MemoryPlacesModel

        fields = [
            "title",
            "address",
            "images",
            "description",
            "review",
        ]
