from rest_framework.routers import DefaultRouter

from games.views import GamesListView

app_name = 'games'

router = DefaultRouter()
router.register('', GamesListView, 'list')

urlpatterns = router.urls
# urlpatterns = [
#     path('', GamesListView.as_view({'get': 'retrieve'}), name='games')
# ]
