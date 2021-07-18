from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'movies', viewsets.MovieViewSet, basename='movies')
router.register(r'ratings', viewsets.RatingViewSet, basename='ratings')

urlpatterns = router.urls