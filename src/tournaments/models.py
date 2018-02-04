import uuid

from django.db import models

from api_v0_1.exceptions.exceptions import NotSupportedFunction
from api_v0_1.models import BaseAPIModel


class Manager(models.Manager):
    def create(self, **kwargs):
        unique_id = uuid.uuid4()

        if 'uuid' not in kwargs:
            kwargs.update({'uuid': unique_id})

        if unique_id.int % 2:
            self._db = 'default'
        else:
            self._db = 'shard_2'

        return super().create(**kwargs)

    def bulk_create(self, objs, batch_size=None):
        raise NotSupportedFunction('`bulk_create` function not supported for shard databases!')


class Tournaments(BaseAPIModel):
    objects = Manager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        uid = self.uuid

        if uid.int % 2:
            using = 'default'
        else:
            using = 'shard_2'

        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = False
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
