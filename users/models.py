import django.contrib.auth.models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import users
from copy import copy


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


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Core(models.Model):
    user = models.OneToOneField(
        User,
        null=False,
        on_delete=models.CASCADE
    )
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    level = models.IntegerField(default=1)

    def click(self, commit=True):
        self.coins += self.click_power

        is_levelupdated = self.is_levelup()

        if is_levelupdated:
            self.level += 1

        if commit:
            self.save()

        return is_levelupdated

    def is_levelup(self):
        return self.coins >= (self.level**2) * 100 * self.level


class Boost(models.Model):
    core = models.ForeignKey(Core, null=False, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    price = models.IntegerField(default=10)
    power = models.IntegerField(default=1)

    def levelup(self):

        if self.core.coins < self.price:
            return False

        self.core.coins -= self.price
        self.core.click_power += self.power
        self.core.save()


        old_boost_values = copy(self)
        self.level += 1
        self.power *= 2
        self.price *= 10
        self.save()

        return old_boost_values, self


