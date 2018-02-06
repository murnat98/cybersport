from api_v0_1.utils import DefaultPagination, ShardingQuerysetOrderingMixin
from api_v0_1.views import DefaultAPIView
from tournaments.models import Tournaments
from tournaments.serializers import TournamentsListSerializer, TournamentDetailSerializer


class TournamentPagination(DefaultPagination):
    pass


class TournamentsView(ShardingQuerysetOrderingMixin, DefaultAPIView):
    model = Tournaments
    pagination_class = TournamentPagination
    list_serializer_class = TournamentsListSerializer
    detail_serializer_class = TournamentDetailSerializer
