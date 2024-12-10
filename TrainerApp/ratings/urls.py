from django.urls import include, path
from rest_framework.routers import DefaultRouter
from TrainerApp.ratings.views import RatingViewSet

router = DefaultRouter()
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
