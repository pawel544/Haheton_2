from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class DieatPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    allergies = models.CharField(max_length=300, unique=False, blank= True)
    food = models.CharField(max_length=300, unique=False, blank= False)
    food_not_like = models.CharField(max_length=300, unique=False, blank=True)
    class StatusDieat(models.TextChoices):
        Redukcja_masy_ciała= "Redukcja masy ciała"
        Budowanie_masy_mięśniowej= "Budowanie masy mięśniowej"
        Ogólny_dobrostan = "Ogólny dobrostan"
    intention = models.CharField(max_length=100,
                                 choices= StatusDieat.choices,
                                 default=StatusDieat.Redukcja_masy_ciała)
    diet_time= models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(120)])