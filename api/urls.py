from django.conf.urls import url, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'location', views.LocationViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
