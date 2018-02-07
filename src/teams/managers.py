import uuid

from api_v0_1.managers import ShardSupportManager
from tournaments.managers import TournamentsManager


class TeamsManager(ShardSupportManager):
    def create(self, **kwargs):
        if 'uuid' not in kwargs:
            kwargs['uuid'] = uuid.uuid4()

        self._db = self.sharding_scheme(uuid=kwargs['uuid'])

        return super().create(**kwargs)

    @staticmethod
    def sharding_scheme(*args, **kwargs):
        """
        Uses the same sharding scheme as the tournaments model.
        """
        return TournamentsManager.sharding_scheme(*args, **kwargs)


class TeamsTournamentsMatchingManager(ShardSupportManager):
    @staticmethod
    def sharding_scheme(*args, **kwargs):
        """
        Sharding in the same database as the tournament is.
        """
        if 'team_uuid' not in kwargs:
            raise KeyError('`team_uuid` required for sharding scheme')

        team_uuid = kwargs['team_uuid']

        return TeamsManager.sharding_scheme(uuid=team_uuid)
