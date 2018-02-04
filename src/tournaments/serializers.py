from rest_framework import serializers

from api_v0_1.serializers import default_serializer_fields
from tournaments.models import Tournaments

tournament_serializer_fields = default_serializer_fields + ('game_uuid',)


class TournamentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = tournament_serializer_fields


class TournamentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = tournament_serializer_fields
