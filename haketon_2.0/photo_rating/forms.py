from django import forms
from .models import TrainingPhoto

class TrainingPhotoForm(forms.ModelForm):
    class Meta:
        model = TrainingPhoto
        fields = ['image']