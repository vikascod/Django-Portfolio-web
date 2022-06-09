from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()

    def __str__(self):
        return self.name
    