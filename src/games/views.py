from rest_framework import viewsets

from api_v0_1.utils import QuerySetOrderingMixin, DefaultPagination
from games.models import Games
from games.serializers import GamesListSerializer, GameDetailSerializer


class GamesView(QuerySetOrderingMixin, viewsets.ModelViewSet):
    pagination_class = DefaultPagination
    model = Games

    def get_serializer_class(self):
        if self.action == 'list':
            return GamesListSerializer

        return GameDetailSerializer
