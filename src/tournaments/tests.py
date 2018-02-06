import json
import uuid

from django.urls import reverse

from api_v0_1.tests import BaseShardingTest
from tournaments.managers import TournamentsManager
from tournaments.models import Tournaments


class TestTournamentShard(BaseShardingTest):
    model = Tournaments
    names = ('tournament', 'a tournament', '1 t', 'some tournament',)
    sorted_names = sorted(names)

    def test_sharding(self):
        for tournament in self.setup_objects:
            self.assertTrue(self._in_right_shard(tournament),
                            msg='Tournament with uuid %s is not in right shard' % tournament.uuid)

    def _get_creation_kwargs(self, name):
        return {'name': name, 'game_uuid': uuid.uuid4()}

    def _in_right_shard(self, obj, *args, **kwargs):
        uid = obj.uuid
        db = TournamentsManager.sharding_scheme(uuid=uid)

        found_in_right_db = True
        try:
            self.model.objects.using(db).get(pk=obj.pk)
        except Tournaments.DoesNotExist:
            found_in_right_db = False

        return found_in_right_db

    def test_order(self):
        response = self.client.get('%s?sort=name' % reverse('api:tournaments-list'))
        content = json.loads(response.content)
        results = content['results']

        results = [result['name'] for result in results]

        self.assertListEqual(results, self.sorted_names)
