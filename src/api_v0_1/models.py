import uuid

from django.db import models


def logo_directory_path(instance, filename):
    return '%s/%s' % (instance.name, filename)


class BaseAPIModel(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, name='uuid', verbose_name='UUID')
    name = models.CharField(max_length=255, name='name', verbose_name='Название')
    description = models.TextField(blank=True, name='description', verbose_name='Описание')
    logo = models.ImageField(blank=True, name='logo', verbose_name='Логотип', upload_to=logo_directory_path)
    created_at = models.DateTimeField(auto_now_add=True, name='created_at', verbose_name='Создан в')

    sharding_data = None

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.sharding_data is not None:
            using = self.manager.sharding_scheme(uuid=self.uuid)

        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True
        ordering = ['name', ]
