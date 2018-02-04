from django.test import TestCase

from tournaments.models import Tournaments


class TestTournamentShard(TestCase):
    names = ('tournament', 'a tournament', '1 t', 'some tournament',)

    def setUp(self):
        self.created_tournaments = []
        for name in self.names:
            self.created_tournaments.append(Tournaments.objects.create(name=name))

    # TODO: write tests

    def tearDown(self):
        for created_tournament in self.created_tournaments:
            created_tournament.delete()
