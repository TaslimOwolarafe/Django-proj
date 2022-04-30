from tkinter import CASCADE
from django.db import models
from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=14)
    email = models.EmailField(max_length=264, unique=True, default="owolarafetaslim@hotmail.com")

    def __str__(self):
        return ("{f} {l}").format(f=self.first_name, l=self.last_name)