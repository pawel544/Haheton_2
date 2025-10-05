from django import forms
from .models import DieatPlan
class DieatForm(forms.ModelForm):
    class Meta:
        model = DieatPlan
        fields= ["allergies","food", "food_not_like","intention", "diet_time"]
        labels = { "allergies": "Podaj czy masz jakieś alergie lub przeciwskazania żywieniowe",
                   "food":"Podaj jakie składniki lubisz ",
                   "food_not_like":"Podaj czego nie lubisz",
                    "intention":"Jaki jest cel diety",
                   "diet_time": "Na ile dni chcesz diete "
            }