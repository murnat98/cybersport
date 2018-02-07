import random
import uuid

from api_v0_1.tests import BaseShardingTest
from matches.models import Matches
from tournaments.managers import TournamentsManager
from tournaments.models import Tournaments


class MatchesShardingTest(BaseShardingTest):
    model = Matches
    iter = ('match 1', 'some match', 'wow match', 'a match',)
    tournament_names = ('tournament 1', 'tournament 2', 'tournament 3', 'tournament 4', 'tournament 5')

    def setUp(self):
        self.tournaments = []
        for name in self.tournament_names:
            self.tournaments.append(Tournaments.objects.create(name=name, game_uuid=uuid.uuid4()))

        super().setUp()

    def tearDown(self):
        for tournament in self.tournaments:
            tournament.delete()

        super().tearDown()

    def test_sharding(self):
        for match in self.setup_objects:
            self.assertTrue(self._in_right_shard(match), msg='Match with uuid %s not found in right db' % match.uuid)

    def _get_creation_kwargs(self, iter_obj):
        tournament_uuids = [obj for obj in Tournaments.objects.using('default').values('uuid')]
        tournament_uuids += [obj for obj in Tournaments.objects.using('shard_2').values('uuid')]

        return {'name': iter_obj, 'tournament_uuid': random.choice(tournament_uuids)['uuid']}

    def _in_right_shard(self, obj, *args, **kwargs):
        tournament_uuid = obj.tournament_uuid

        db = TournamentsManager.sharding_scheme(uuid=tournament_uuid)

        in_right_db = True
        try:
            self.model.objects.using(db).get(pk=obj.pk)
        except self.model.DoesNotExist:
            in_right_db = False

        return in_right_db
