from django.db import models

from api_v0_1.models import BaseAPIModel
from matches.managers import MatchesManager
from tournaments.models import Tournaments

tournaments = ((tournament.uuid, tournament.name) for tournament in Tournaments.objects.all())  # TODO: cache this


class Matches(BaseAPIModel):
    tournament_uuid = models.UUIDField(choices=tournaments, name='tournament_uuid', verbose_name='Турнир')

    manager = MatchesManager
    objects = manager()

    def shard(self):
        return self.manager.sharding_scheme(tournament_uuid=self.tournament_uuid)

    class Meta:
        abstract = False
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'
