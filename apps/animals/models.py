from django.db import models

# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=255)
    fact = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_urls  = models.CharField(max_length=255)

    class Meta:
        db_table='animals'
    
    def __str__(self):
        return self.name