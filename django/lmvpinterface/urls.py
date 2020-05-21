from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'commits', views.CommitViewSet)
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')), #from the DRF quickstart, to allow login url for browseable API
]
