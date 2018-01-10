from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from . import serializers
from core.models import HigherEducationInstitution, LearningOpportunitySpecification, OrganizationalUnit


class HigherEducationInstitutionModelViewSet(viewsets.ModelViewSet):
    """
    Higher Education Institution List.

    Dynamic title filter can be added with `q` parameter.
    """
    serializer_class = serializers.HigherEducationInstitutionSerializer
    queryset = HigherEducationInstitution.objects.all().order_by('name')
    filter_backends = (SearchFilter, )
    search_fields = ('^name', )


class OrganizationalUnitViewSet(viewsets.ModelViewSet):
    """
    Organizational Unit List.

    It's mandatory to indicate a hei's uuid.
    Dynamic title filter can be added with `q` parameter.
    """
    serializer_class = serializers.OrganizationalUnitSerializer
    queryset = OrganizationalUnit.objects.all().order_by('name')
    filter_backends = (SearchFilter, )
    search_fields = ('^name', )


class LearningOpportunitySpecificationModelViewSet(viewsets.ModelViewSet):
    """
    Learning Opportunity Specification List.

    It's mandatory to indicate a hei's uuid.
    Dynamic title filter can be added with `q` parameter.
    """
    serializer_class = serializers.LearningOpportunitySpecificationSerializer
    queryset = LearningOpportunitySpecification.objects.all().order_by('title')
    filter_backends = (SearchFilter, )
    search_fields = ('^title', )
