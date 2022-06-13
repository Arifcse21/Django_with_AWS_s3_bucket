from .models import SimpleFormModel
from django import forms



class SimpleForm(forms.ModelForm):
    class Meta:
        model = SimpleFormModel
        fields = [
                "name",
                "image",
         ]
