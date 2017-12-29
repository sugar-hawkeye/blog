from django.db import models

# Create your models here.
class GUIDModel(models.Model):
    id = models.UUIDField()
    pass