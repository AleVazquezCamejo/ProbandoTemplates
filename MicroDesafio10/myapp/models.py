from django.db import models

# Create your models here.


class cliente(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
    email= models.EmailField()