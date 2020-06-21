from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'commits', views.CommitViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'metrics', views.MetricViewSet)
router.register(r'properties', views.PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')), #from the DRF quickstart, to allow login url for browseable API
]
