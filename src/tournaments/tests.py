import json

from django.test import TestCase
from django.urls import reverse

from tournaments.models import Tournaments


class TestTournamentShard(TestCase):
    names = ('tournament', 'a tournament', '1 t', 'some tournament',)
    sorted_names = sorted(names)

    def setUp(self):
        self.created_tournaments = []
        for name in self.names:
            self.created_tournaments.append(Tournaments.objects.create(name=name))

    def test_sharding(self):
        for tournament in self.created_tournaments:
            uid = tournament.uuid

            if uid.int % 2:
                db = 'default'
            else:
                db = 'shard_2'

            found_in_right_db = True
            try:
                Tournaments.objects.using(db).filter(name=tournament.name)
            except Tournaments.DoesNotExist:
                found_in_right_db = False

            self.assertTrue(found_in_right_db)

    def test_order(self):
        response = self.client.get('%s?sort=name' % reverse('api:tournaments-list'))
        content = json.loads(response.content)
        results = content['results']

        results = [result['name'] for result in results]

        self.assertListEqual(results, self.sorted_names)

    def tearDown(self):
        for created_tournament in self.created_tournaments:
            created_tournament.delete()
