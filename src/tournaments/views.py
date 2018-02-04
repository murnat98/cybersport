from api_v0_1.utils import DefaultPagination
from api_v0_1.views import DefaultAPIView
from tournaments.models import Tournaments
from tournaments.serializers import TournamentsListSerializer, TournamentDetailSerializer


class TournamentPagination(DefaultPagination):
    pass


class TournamentsView(DefaultAPIView):
    model = Tournaments
    pagination_class = TournamentPagination
    list_serializer_class = TournamentsListSerializer
    detail_serializer_class = TournamentDetailSerializer

    def get_queryset(self):
        sort_parameter = self.get_sort_parameter()

        queryset = super().get_queryset()

        shard_1_queryset = [obj for obj in queryset.using('default')]
        shard_2_queryset = [obj for obj in queryset.using('shard_2')]

        result_queryset = sorted(shard_1_queryset + shard_2_queryset,
                                 key=lambda tournament: getattr(tournament, sort_parameter), reverse=self.is_desc())

        return result_queryset
