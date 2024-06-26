from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Пользовательская модель пользователя.

    Поля:
    - email: Адрес электронной почты пользователя.
    - bio: Биография пользователя.
    - first_name: Имя пользователя.
    - last_name: Фамилия пользователя.
    """
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=50,
        unique=True,
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
        null=True
    )

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'
