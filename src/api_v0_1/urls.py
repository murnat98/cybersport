from rest_framework.routers import SimpleRouter

from api_v0_1.views import GamesView

app_name = 'games'

router = SimpleRouter()
router.register('games', GamesView, 'games')

urlpatterns = router.urls
