from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.price < 100:
            return
        super().save(*args, **kwargs) #avoid cheap products

    def __str__(self):
        return self.name
