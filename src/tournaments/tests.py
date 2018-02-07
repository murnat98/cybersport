import json
import uuid

from django.urls import reverse

from api_v0_1.tests import BaseShardingTest
from tournaments.models import Tournaments


class TestUUIDSharding(BaseShardingTest):
    model = Tournaments
    names = ('tournament', 'a tournament', '1 t', 'some tournament',)
    sorted_names = sorted(names)

    def _get_creation_kwargs(self, name):
        return {'name': name, 'game_uuid': uuid.uuid4()}

    def _in_right_shard(self, obj, *args, **kwargs):
        assert isinstance(obj, self.model)

        db = self.model.manager.sharding_scheme(uuid=obj.uuid)

        found_in_right_db = True
        try:
            self.model.objects.using(db).get(pk=obj.pk)
        except self.model.DoesNotExist:
            found_in_right_db = False

        return found_in_right_db


class ShardTest(TestUUIDSharding):
    def test_sharding(self):
        for obj in self.setup_objects:
            self.assertTrue(self._in_right_shard(obj),
                            msg='%s with uuid %s is not in right shard' % (
                                self.model.__name__, obj.uuid
                            ))


class OrderTest(TestUUIDSharding):
    def test_order(self):
        response = self.client.get('%s?sort=name' % reverse('api:tournaments-list'))
        content = json.loads(response.content)
        results = content['results']

        results = [result['name'] for result in results]

        self.assertListEqual(results, self.sorted_names)
