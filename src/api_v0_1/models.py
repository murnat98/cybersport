from django.db import models


def logo_directory_path(instance, filename):
    return '%s/%s' % (instance.name, filename)


class BaseAPIModel(models.Model):
    name = models.CharField(max_length=255, name='name', verbose_name='Название')
    description = models.TextField(blank=True, name='description', verbose_name='Описание')
    logo = models.ImageField(blank=True, name='logo', verbose_name='Логотип', upload_to=logo_directory_path)
    created_at = models.DateTimeField(auto_now_add=True, name='created_at', verbose_name='Создан в')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name', ]
