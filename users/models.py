from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя с дополнительными полями.
    """

    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(
        default=True
    )  # Используется для проверки прав доступа к API

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
