from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(primary_key=True, null=False, blank=False)
    password = models.CharField(null=False, blank=False)
    name = models.CharField(null=False, blank=False)
    number = models.DecimalField(null=False, blank=False)
