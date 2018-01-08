from django.urls.conf import path

from api import views


urlpatterns = [
    path('hei', views.HEIModelViewSet.as_view({'get': 'list'})),
    path('los/hei/<uuid:id>', views.LOSModelViewSet.as_view({'get': 'list'}))
]
