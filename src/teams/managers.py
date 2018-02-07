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
