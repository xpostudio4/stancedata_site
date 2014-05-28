from django.db import models

# Create your models here.

class Event(models.Model):
    title =  models.CharField(max_length=200)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    description = models.TextField()
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


