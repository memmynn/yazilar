from django.db import models
from django.utils import timezone


class Post(models.Model):
    yazar = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    yazi = models.TextField()
    tarih = models.DateTimeField(
        default=timezone.now)

    def yayımla(self):
        self.save()


# Create your models here.
