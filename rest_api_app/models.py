from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    price = models.IntegerField()

    def __str__(self):
        return self.name




