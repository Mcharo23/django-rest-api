from django.db import models

# Create your models here.


class Products(models.Model):
    p_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
