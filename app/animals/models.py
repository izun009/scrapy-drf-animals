from django.db import models

class Animals(models.Model):
    name = models.CharField(max_length=255)
    facts = models.CharField(max_length=255)
    image_urls = models.CharField(max_length=255)

    class Meta:
        db_table = 'animals'

    def __str__(self):
        return self.name