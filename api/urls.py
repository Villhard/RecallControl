from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import WordViewSet, StudyView


router_v1 = DefaultRouter()
router_v1.register("words", WordViewSet, basename="word")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/study/", StudyView.as_view(), name="study"),
]
