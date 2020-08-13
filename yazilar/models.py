from django.db import models
from django.utils import timezone


class Yazi(models.Model):
    yazi = models.TextField()
    başlık = models.CharField(max_length=50, default='')
    tarih = models.DateTimeField(
        default=timezone.now)

    def yayimla(self):
        self.save()


# Create your models here.
