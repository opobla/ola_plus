from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^$', views.TestViewSet.as_view({
        'get': 'list',
        'post': 'create',

    })),
]
