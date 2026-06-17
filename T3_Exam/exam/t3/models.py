from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    url = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    def __str__(self):
        return self.name