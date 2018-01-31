from django.db import models


def game_logo_directory_path(instance, filename):
    return 'games/%s' % filename


class Games(models.Model):
    name = models.CharField(max_length=255, name='name', verbose_name='Название')
    description = models.TextField(blank=True, name='description', verbose_name='Описание')
    logo = models.ImageField(blank=True, name='logo', verbose_name='Логотип', upload_to=game_logo_directory_path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
