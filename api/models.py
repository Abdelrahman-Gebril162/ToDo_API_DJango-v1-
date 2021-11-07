from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(max_length=None)

    def __str__(self):
        return self.name