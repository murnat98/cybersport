from rest_framework import viewsets

from games.models import Games
from games.serializers import GamesListSerializer
from games.utils import QuerySetOrderingMixin, DefaultPagination


class GamesListView(QuerySetOrderingMixin, viewsets.ModelViewSet):
    serializer_class = GamesListSerializer
    pagination_class = DefaultPagination
    model = Games
