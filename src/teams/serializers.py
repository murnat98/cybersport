from rest_framework import serializers

from api_v0_1.serializers import default_serializer_fields
from teams.models import Teams

team_serializer_fields = default_serializer_fields


class TeamsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = team_serializer_fields


class TeamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = team_serializer_fields
