import uuid

from django.db import models

from api_v0_1.models import BaseAPIModel, BaseShardingModel
from teams.managers import TeamsManager, TeamsTournamentsMatchingManager
from tournaments.models import Tournaments


class Teams(BaseAPIModel):
    manager = TeamsManager
    objects = manager()

    def shard(self):
        return self.manager.sharding_scheme(uuid=uuid.uuid4())

    class Meta:
        abstract = False
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


tournaments = ((tournament.uuid, tournament.name) for tournament in Tournaments.objects.all())  # TODO: cache this
teams = ((teams.uuid, teams.name) for teams in Teams.objects.all())  # TODO: cache this


class TeamsTournamentsMatching(BaseShardingModel):
    tournament_uuid = models.UUIDField(choices=tournaments, name='tournament_uuid', verbose_name='Турнир')
    team_uuid = models.UUIDField(choices=teams, name='team_uuid', verbose_name='Команда')

    manager = TeamsTournamentsMatchingManager
    objects = manager()

    def shard(self):
        return self.manager.sharding_scheme(team_uuid=self.team_uuid)

    class Meta:
        abstract = False
