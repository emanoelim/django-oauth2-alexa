from rest_framework import routers
from django.urls import path, include

from info.views import InfoViewSet


router = routers.DefaultRouter()
router.register('infos', InfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
