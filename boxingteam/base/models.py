from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TypeExercise(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class User(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(blank=True)
    section = models.ForeignKey(TypeExercise, on_delete=models.SET_NULL, null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
