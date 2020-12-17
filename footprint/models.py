from django.db import models

# Create your models here.
class Footprint(models.Model):
    date = models.CharField(max_length=100)
    footprint = models.CharField(max_length=100)
    

    def __str__(self):
        return self.date