from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class CustomBaseUserManager(BaseUserManager):

    def create_user(self, age, email, username, password=None ):
        if not email:
            raise ValueError("You need an email address")

        user = self.model(
            email=self.normalize_email(email),
            age=age,
            username=username,
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, age, email, username, password):
        user = self.create_user(
            age,
            email,
            username,
            password
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractUser):

    age = models.PositiveIntegerField()
    bio = models.CharField(max_length=140)
    email = models.EmailField(unique=True, blank=False, max_length=254, verbose_name='email address')

    objects = CustomBaseUserManager

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['age', 'username']

    def __str__(self):
        return self.email

