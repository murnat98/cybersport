from api_v0_1.views import DefaultAPIView
from games.models import Games
from games.serializers import GamesListSerializer, GameDetailSerializer


class GamesView(DefaultAPIView):
    model = Games
    list_serializer_class = GamesListSerializer
    detail_serializer_class = GameDetailSerializer
