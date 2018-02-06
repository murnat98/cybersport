from api_v0_1.utils import ShardingQuerysetOrderingMixin
from api_v0_1.views import DefaultAPIView
from matches.models import Matches
from matches.serializers import MatchesListSerializer, MatchDetailSerializer


class MatchesView(ShardingQuerysetOrderingMixin, DefaultAPIView):
    model = Matches
    list_serializer_class = MatchesListSerializer
    detail_serializer_class = MatchDetailSerializer
