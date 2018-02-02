# Generated by Django 2.0.1 on 2018-02-02 11:13

import django.utils.timezone
from django.db import migrations, models

import games.models


class Migration(migrations.Migration):
    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ['name'], 'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AddField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан в'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='games',
            name='logo',
            field=models.ImageField(blank=True, upload_to=games.models.game_logo_directory_path,
                                    verbose_name='Логотип'),
        ),
    ]
