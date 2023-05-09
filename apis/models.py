from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.TextField(
        max_length=20,
        default='anonymous',
    )
    age = models.IntegerField(
        null=True
    )
    title = models.TextField(
        null=False
    )
    context = models.TextField(
        max_length=255
    )