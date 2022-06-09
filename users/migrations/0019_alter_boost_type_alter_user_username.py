# Generated by Django 4.0.3 on 2022-06-09 20:59

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'auto'), (0, 'casual')], default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Такой пользователь уже зарегестрирован.'}, help_text='', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
