from django.urls import path
urlpatterns = [
    re_path(r'^api-auth/', include('rest_framework.urls')), #from the DRF quickstart, to allow login url for browseable API
]
