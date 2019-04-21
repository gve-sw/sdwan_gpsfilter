from django.db import models

class User(models.Model):
    def __str__(self):
        return self.login_name

    login_name = models.CharField(max_length=15)
    password = models.CharField(max_length=64)
    country = models.CharField(max_length=30)
    # Access rights will store JSON list of allowed countries to view
    access_rights = models.CharField(max_length=200)

# Create your models here.
