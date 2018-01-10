from django.urls.conf import path
from api import views


urlpatterns = [
    path('hei', views.HigherEducationInstitutionModelViewSet.as_view({'get': 'list'})),
    path('hei/<uuid:id>', views.OrganizationalUnitViewSet.as_view({'get': 'list'})),
    path('los/hei/<uuid:id>', views.LearningOpportunitySpecificationModelViewSet.as_view({'get': 'list'}))
]
