from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile = models.ImageField(verbose_name="profile picture", null=True, blank=True)


class Posts(models.Model):
    description = models.fields.TextField()
    image = models.ImageField(verbose_name="Post Pic", null=True, blank=True)
    writen_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
