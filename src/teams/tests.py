import random
import string
import uuid

from api_v0_1.tests import BaseShardingTest
from teams.managers import TeamsTournamentsMatchingManager
from teams.models import Teams, TeamsTournamentsMatching
from tournaments.models import Tournaments
from tournaments.tests import TestUUIDSharding, ShardTest


def generate_random_strings(tuple_length=None, string_length=None):
    """
    Generates random strings tuple.
    :param tuple_length: the tuple's length. Defaults to 100.
    :param string_length: string's length. Defaults to random integer from 1 to 10.
    :return: string tuple
    """
    tuple_length = tuple_length or 100
    string_length = string_length or random.randint(1, 10)

    return [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(string_length)) for _ in
            range(tuple_length)]


class TeamsTest(TestUUIDSharding, ShardTest):
    model = Teams
    iter = generate_random_strings()

    def _get_creation_kwargs(self, iter_obj):
        return {'name': iter_obj}


class TeamsTournamentsMatchingTest(BaseShardingTest):
    model = TeamsTournamentsMatching
    tournament_names = generate_random_strings()
    team_names = generate_random_strings()

    def setUp(self):
        super().setUp()

        self.tournaments = []
        self.teams = []
        for tournament_name in self.tournament_names:
            self.tournaments.append(Tournaments.objects.create(name=tournament_name, game_uuid=uuid.uuid4()))

        for team_name in self.team_names:
            self.teams.append(Teams.objects.create(name=team_name))

    def tearDown(self):
        super().tearDown()

        for tournament in self.tournaments:
            tournament.delete()

        for team in self.teams:
            team.delete()

    def _get_creation_kwargs(self, iter_obj):
        return {
            'tournament_uuid': random.choice(self.tournaments)['uuid'],
            'team_uuid': random.choice(self.teams)['uuid']
        }

    def _in_right_shard(self, obj, *args, **kwargs):
        assert isinstance(obj, TeamsTournamentsMatching)

        team_uuid = obj.team_uuid

        return TeamsTournamentsMatchingManager.sharding_scheme(team_uuid=team_uuid)

    def test_shard(self):
        for obj in self.setup_objects:
            self.assertTrue(self._in_right_shard(obj),
                            msg='Tournament-team match with uuid %s not found in right database' % obj.uuid)
