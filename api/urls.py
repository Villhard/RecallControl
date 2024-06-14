from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import WordViewSet



router_v1 = SimpleRouter()
router_v1.register("words", WordViewSet)

urlpatterns = [
    path("", include(router_v1.urls))
]
