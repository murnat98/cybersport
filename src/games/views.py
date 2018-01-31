from rest_framework import viewsets

from games.models import Games
from games.serializers import GamesListSerializer


class GamesListView(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesListSerializer
