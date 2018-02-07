from api_v0_1.utils import ShardingQuerysetOrderingMixin
from api_v0_1.views import DefaultAPIView
from teams.models import Teams, TeamsTournamentsMatching
from teams.serializers import TeamsListSerializer, TeamDetailSerializer, TeamsTournamentsMatchListSerializer, \
    TeamsTournamentMatchDetailSerializer


class TeamsView(ShardingQuerysetOrderingMixin, DefaultAPIView):
    model = Teams
    list_serializer_class = TeamsListSerializer
    detail_serializer_class = TeamDetailSerializer


class TeamsTournamentsMatchingView(ShardingQuerysetOrderingMixin, DefaultAPIView):
    model = TeamsTournamentsMatching
    list_serializer_class = TeamsTournamentsMatchListSerializer
    detail_serializer_class = TeamsTournamentMatchDetailSerializer
    default_sort_parameter = 'uuid'
