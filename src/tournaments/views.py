from api_v0_1.views import DefaultAPIView
from tournaments.models import Tournaments
from tournaments.serializers import TournamentsListSerializer, TournamentDetailSerializer


class TournamentsView(DefaultAPIView):
    model = Tournaments
    list_serializer_class = TournamentsListSerializer
    detail_serializer_class = TournamentDetailSerializer
