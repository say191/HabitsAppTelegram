from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.CharField(max_length=40, unique=True, verbose_name='email')
    phone = models.CharField(max_length=20, **NULLABLE, verbose_name='phone')
    city = models.CharField(max_length=20, **NULLABLE, verbose_name='city')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='image')
    chat_id = models.CharField(max_length=30, verbose_name='chat_id', **NULLABLE)
    telegram_id = models.CharField(max_length=30, unique=True, verbose_name='telegram_id')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
