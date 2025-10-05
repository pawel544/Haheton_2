from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.



class Gym(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Status_place(models.TextChoices):
        Dom= "Hause"
        Siłownia = "Siłownia"
    place = models.CharField(max_length=30,
                             choices=Status_place.choices,
                             default=Status_place.Dom)
    age = models.IntegerField(
        validators=[MinValueValidator(18),
                    MaxValueValidator(120)])
    libra= models.IntegerField(
        validators=[MinValueValidator(35),
                    MaxValueValidator(350)])
    n_exercise= models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)])
    experience = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(40)])
    class Status(models.TextChoices):
        Redukcja_tkanki_tłuszczowej_i_utrata_wagi= "Redukcja tkanki tłuszczowej i utrata wagi"
        Budowanie_masy_mięśniowej= "Budowanie masy mięśniowej"
        Poprawa_jakości_mięśni = "Poprawa jakości mięśni"
        Zwiększenie_wydolności = "Zwiększenie wydolności"
        Poprawa_elastyczności_i_ruchomości = "Poprawa elastyczności i ruchomości"
        zdrowie = "Poprawa zdrowia układu krążenia"
        Korekcja_wad_postawy = "Korekcja wad postawy"
        Relaksacja_i_redukcja_stresu = "Relaksacja i redukcja stresu"
        Poprawa_samopoczucia ="Poprawa samopoczucia"
    objective = models.CharField(max_length=100,
                                 choices= Status.choices,
                                 default=Status.Redukcja_tkanki_tłuszczowej_i_utrata_wagi)



