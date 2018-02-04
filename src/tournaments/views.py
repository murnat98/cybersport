from api_v0_1.views import DefaultAPIView
from tournaments.models import Tournaments
from tournaments.serializers import TournamentsListSerializer, TournamentDetailSerializer


class TournamentsView(DefaultAPIView):
    model = Tournaments
    list_serializer_class = TournamentsListSerializer
    detail_serializer_class = TournamentDetailSerializer

    def get_queryset(self):
        # TODO: sort it before returning the list
        # first_queryset = [obj for obj in super().get_queryset()]
        # second_queryset = [obj for obj in first_queryset.using('shard_2')]

        return [obj for obj in super().get_queryset()] + [obj for obj in super().get_queryset().using('shard_2')]
