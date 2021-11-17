from django.db import models
from django.db.models.deletion import CASCADE

class Profile(models.Model):
    nama = models.CharField(max_length=250, blank=True, verbose_name='nama')
    tanggal_lahir = models.DateField(blank=True)

class Alamat(models.Model):
    user = models.OneToOneField(Profile, on_delete=CASCADE)
    alamat = models.TextField(max_length=500, blank=True, verbose_name='alamat')