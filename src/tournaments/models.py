from django.db import models

from api_v0_1.models import BaseAPIModel
from games.models import Games
from tournaments.managers import TournamentsManager

games = ((game.uuid, game.name) for game in Games.objects.all())


class Tournaments(BaseAPIModel):
    game_uuid = models.UUIDField(name='game_uuid', verbose_name='Игра', choices=games)

    manager = TournamentsManager
    objects = manager()

    class Meta:
        abstract = False
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
