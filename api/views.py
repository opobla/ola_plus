from rest_framework import viewsets, filters
from . import serializers
from core.models import HigherEducationInstitution, LearningOpportunitySpecification, OrganizationalUnit


class HigherEducationInstitutionModelViewSet(viewsets.ModelViewSet):
    """
    Higher Education Institution List.

    Dynamic Higher Education Institution's name filter can be added with `q` parameter.
    """
    serializer_class = serializers.HigherEducationInstitutionSerializer
    queryset = HigherEducationInstitution.objects.all().order_by('name')
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )


class OrganizationalUnitViewSet(viewsets.ModelViewSet):
    """
    Organizational Unit List.

    **It's mandatory to provide an Higher Education Institution UUID.**

    Dynamic Organizational Unit's name filter can be added with `q` parameter.
    """
    serializer_class = serializers.OrganizationalUnitSerializer
    queryset = OrganizationalUnit.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )

    def get_queryset(self):
        return self.queryset\
            .filter(higher_education_institution_id=self.kwargs["id"]) \
            .order_by('name')


class LearningOpportunitySpecificationModelViewSet(viewsets.ModelViewSet):
    """
    Learning Opportunity Specification List.

    **It's mandatory to provide an Organizational Unit UUID.**

    Dynamic Learning Opportunity Specification's title filter can be added with `q` parameter.
    """
    serializer_class = serializers.LearningOpportunitySpecificationSerializer
    queryset = LearningOpportunitySpecification.objects.all().order_by('title')
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', )

    def get_queryset(self):
        return self.queryset \
            .filter(organizational_unit_id=self.kwargs["id"]) \
            .order_by('title')
