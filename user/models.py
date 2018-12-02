from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    age = models.PositiveIntegerField()
    bio = models.CharField(max_length=140)


