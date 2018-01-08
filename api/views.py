from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from api.serializers import HigherEducationInstitutionSerializer, LearningOpportunitySpecificationSerializer
from core.models import HigherEducationInstitution, LearningOpportunitySpecification


class HEIModelViewSet(viewsets.ModelViewSet):
    serializer_class = HigherEducationInstitutionSerializer
    queryset = HigherEducationInstitution.objects.all().order_by('name')
    filter_backends = (SearchFilter, )
    search_fields = ('^name', )


class LOSModelViewSet(viewsets.ModelViewSet):
    serializer_class = LearningOpportunitySpecificationSerializer
    queryset = LearningOpportunitySpecification.objects.all().order_by('title')
    filter_backends = (SearchFilter, )
    search_fields = ('^title', )
