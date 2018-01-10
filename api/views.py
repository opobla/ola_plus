from rest_framework import viewsets
from . import serializers
from core.models import HigherEducationInstitution, LearningOpportunitySpecification, OrganizationalUnit


class HigherEducationInstitutionModelViewSet(viewsets.ModelViewSet):
    """
    Higher Education Institution List.

    Dynamic title filter can be added with `q` parameter.
    """
    serializer_class = serializers.HigherEducationInstitutionSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        queryset = HigherEducationInstitution.objects.all().order_by('name')
        if q:
            return queryset.filter(name__icontains=q)
        return queryset


class OrganizationalUnitViewSet(viewsets.ModelViewSet):
    """
    Organizational Unit List.

    It's mandatory to indicate a hei's uuid.

    Dynamic title filter can be added with `q` parameter.
    """
    serializer_class = serializers.OrganizationalUnitSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        queryset = OrganizationalUnit.objects.all()\
            .filter(higher_education_institution_id=self.kwargs["id"])\
            .order_by('name')
        if q:
            return queryset.filter(name__icontains=q)
        return queryset


class LearningOpportunitySpecificationModelViewSet(viewsets.ModelViewSet):
    """
    Learning Opportunity Specification List.

    It's mandatory to indicate a hei's uuid.

    Dynamic title filter can be added with `q` parameter.
    """
    serializer_class = serializers.LearningOpportunitySpecificationSerializer

    def get_queryset(self):
        queryset = LearningOpportunitySpecification.objects.all() \
            .filter(organizational_unit_id=self.kwargs["id"]) \
            .order_by('title')
        q = self.request.query_params.get('q', None)
        if q:
            return queryset.filter(title__icontains=q)
        return queryset
