from rest_framework import serializers

from api_v0_1.serializers import default_serializer_fields
from tournaments.models import Tournaments


class TournamentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = default_serializer_fields


class TournamentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = default_serializer_fields
