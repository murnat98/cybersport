import uuid

from django.db import models

from api_v0_1.models import BaseAPIModel
from games.models import Games
from tournaments.managers import TournamentsManager

games = ((game.uuid, game.name) for game in Games.objects.all())  # TODO: cache this


class Tournaments(BaseAPIModel):
    game_uuid = models.UUIDField(choices=games, name='game_uuid', verbose_name='Игра')

    manager = TournamentsManager
    objects = manager()

    def shard(self):
        return self.manager.sharding_scheme(uuid=uuid.uuid4())

    class Meta:
        abstract = False
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
