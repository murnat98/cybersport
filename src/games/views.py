from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from games.models import Games
from games.serializers import GamesListSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 10


class GamesPagination(DefaultPagination):
    pass


class GamesListView(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesListSerializer
    pagination_class = GamesPagination
