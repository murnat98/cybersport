import json

from django.test import TestCase
from django.urls import reverse

from games.models import Games


class TestGamesSorting(TestCase):
    def setUp(self):
        Games.objects.create(name='name_a', description='description_a')
        Games.objects.create(name='name_z', description='a description')
        Games.objects.create(name='name_a2', description='some description')

    def test_games_order_by_name(self):
        name_field = 'name'

        response = self.client.get(reverse('api:games-list'))
        content = json.loads(response.content)
        results = content['results']

        name_1 = results[0][name_field]
        name_2 = results[1][name_field]
        name_3 = results[2][name_field]

        self.assertEquals(name_1, 'name_a')
        self.assertEquals(name_2, 'name_a2')
        self.assertEquals(name_3, 'name_z')

    def test_games_order_by_description(self):
        description_field = 'description'

        response = self.client.get('%s?sort=description&desc' % reverse('api:games-list'))
        content = json.loads(response.content)
        results = content['results']

        description_1 = results[0][description_field]
        description_2 = results[1][description_field]
        description_3 = results[2][description_field]

        self.assertEquals(description_3, 'a description')
        self.assertEquals(description_2, 'description_a')
        self.assertEquals(description_1, 'some description')

    def test_games_order_by_unknown_field(self):
        name_field = 'name'

        response = self.client.get('%s?sort=not_existing_field' % reverse('api:games-list'))
        content = json.loads(response.content)
        results = content['results']

        name_1 = results[0][name_field]
        name_2 = results[1][name_field]
        name_3 = results[2][name_field]

        self.assertEquals(name_1, 'name_a')
        self.assertEquals(name_2, 'name_a2')
        self.assertEquals(name_3, 'name_z')
