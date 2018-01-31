from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=255, name='name', verbose_name='Название')
    description = models.TextField(blank=True, name='description', verbose_name='Описание')
    logo = models.ImageField(blank=True, name='logo', verbose_name='Логотип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
