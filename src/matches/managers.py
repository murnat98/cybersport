from api_v0_1.managers import ShardSupportManager
from matches.exceptions import TournamentNotFoundError
from tournaments.models import Tournaments


class MatchesManager(ShardSupportManager):
    def create(self, **kwargs):
        self._db = self.sharding_scheme(tournament_uuid=kwargs['tournament_uuid'])

        return super().create(**kwargs)

    @staticmethod
    def sharding_scheme(*args, **kwargs):
        """
        Sharding matches in the same database as the tournament is.
        """
        databases = ('default', 'shard_2')

        if 'tournament_uuid' not in kwargs:
            raise KeyError('`sharding_scheme` requires tournament_uuid for sharding')

        tournament_uuid = kwargs['tournament_uuid']

        shard_database = None
        for database in databases:
            try:
                Tournaments.objects.using(database).get(uuid=tournament_uuid)
            except Tournaments.DoesNotExist:
                pass
            else:
                shard_database = database

        if shard_database is not None:
            return shard_database
        else:
            raise TournamentNotFoundError(
                'Tournament with uuid %s not found. in databases %s' % (tournament_uuid, databases))
