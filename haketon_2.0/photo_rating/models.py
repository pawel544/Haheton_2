from django.db import models
from django.contrib.auth.models import User

class TrainingPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='training_photos', blank=True, null= False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analysis_result = models.TextField(blank=True, null=True)  # wynik AI

    def __str__(self):
        return f"Zdjęcie treningowe {self.user.username} ({self.uploaded_at})"