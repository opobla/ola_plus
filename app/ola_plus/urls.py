"""ola_plus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from demo_algolia.views import InstantSearchView
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(title="OLA+ API",
                default_version='v1',
                description="Test description",
                terms_of_service="https://www.google.com/policies/terms/",
                contact=openapi.Contact(email="contact@snippets.local"),
                license=openapi.License(name="BSD License")),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny, ),
)


urlpatterns = [
    path('swagger.json', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),

    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('demo/', InstantSearchView.as_view(template_name="instant_search_view.html")),
]

if settings.DEBUG:
    pass
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
