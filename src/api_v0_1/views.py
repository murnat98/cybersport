from rest_framework import viewsets

from api_v0_1.utils import QuerySetOrderingMixin, DefaultPagination
from games.models import Games
from games.serializers import GamesListSerializer


class GamesView(QuerySetOrderingMixin, viewsets.ModelViewSet):
    serializer_class = GamesListSerializer
    pagination_class = DefaultPagination
    model = Games
