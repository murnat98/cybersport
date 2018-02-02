from rest_framework.routers import DefaultRouter

from api_v0_1.views import GamesView

app_name = 'games'

router = DefaultRouter()
router.register('games', GamesView, 'retrieve')

urlpatterns = router.urls
