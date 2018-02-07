from rest_framework import serializers

from api_v0_1.serializers import default_serializer_fields
from teams.models import Teams, TeamsTournamentsMatching

team_serializer_fields = default_serializer_fields
teams_tournaments_matching_fields = ('uuid', 'tournament_uuid', 'team_uuid')


class TeamsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = team_serializer_fields


class TeamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = team_serializer_fields


class TeamsTournamentsMatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamsTournamentsMatching
        fields = teams_tournaments_matching_fields


class TeamsTournamentMatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamsTournamentsMatching
        fields = teams_tournaments_matching_fields
