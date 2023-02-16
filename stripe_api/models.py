from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
