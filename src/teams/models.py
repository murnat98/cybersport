import uuid

from api_v0_1.models import BaseAPIModel
from teams.managers import TeamsManager


class Teams(BaseAPIModel):
    manager = TeamsManager
    objects = manager()

    def shard(self):
        return self.manager.sharding_scheme(uuid=uuid.uuid4())

    class Meta:
        abstract = False
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
