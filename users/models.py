import django.contrib.auth.models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

import users


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            ""
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Такой пользователь уже зарегестрирован."),
        },
    )


class Core(models.Model):
    user = models.OneToOneField(
        User,
        null=False,
        on_delete=models.CASCADE
    )
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)

    def click(self, commit=True):
        self.coins += self.click_power
        if commit:
            self.save()
        return self.coins


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
