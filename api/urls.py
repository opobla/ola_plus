from django.urls.conf import path
from api import views


urlpatterns = [
    path('hei', views.HigherEducationInstitutionModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('hei/<uuid:id>', views.OrganizationalUnitTreeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('ounit/<uuid:id>', views.OrganizationalUnitViewSet.as_view({'get': 'list'})),
    path('los/<uuid:id>', views.LearningOpportunitySpecificationModelViewSet.as_view({'get': 'list'})),
    path('los', views.LearningOpportunitySpecificationModelViewSet.as_view({'post': 'create'}))
]
