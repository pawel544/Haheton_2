from django import forms
from .models import Gym

class GymForms(forms.ModelForm):
    class Meta:
        model = Gym
        fields = ['place','age','libra','n_exercise','experience','objective']
        labels = {'place':' Wybież miejsce treningu',
                  'age': 'Podaj swój wiek ',
                  'libra' : 'Podaj swoją wage(kg)',
                  'n_exercise': 'Ile ćwiczeń maxsymalnie na jedną partnie 10',
                  'experience': 'Podaj jak długo już ćwiczysz',
                  'objective': 'Wybież swój cel'}
