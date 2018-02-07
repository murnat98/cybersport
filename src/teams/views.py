from api_v0_1.utils import ShardingQuerysetOrderingMixin
from api_v0_1.views import DefaultAPIView
from teams.models import Teams
from teams.serializers import TeamsListSerializer, TeamDetailSerializer


class TeamsView(ShardingQuerysetOrderingMixin, DefaultAPIView):
    model = Teams
    list_serializer_class = TeamsListSerializer
    detail_serializer_class = TeamDetailSerializer
