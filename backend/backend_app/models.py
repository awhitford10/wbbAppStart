from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

class Dog(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
