from rest_framework import viewsets, filters
from . import serializers
from core.models import HigherEducationInstitution, LearningOpportunitySpecification, OrganizationalUnit


class HigherEducationInstitutionModelViewSet(viewsets.ModelViewSet):
    """
    Higher Education Institutions.

    create:
    Create a new HEI by giving a name and a email (do not specify origin)

    list:
    This endpoint retrieves all the available HEI's.
    Since the list can be potentially very long, it is possible to filter this list by giving a URL parameter q with
    a text string. The list then will contain only HEI's whose names include the given text string. Note that demo
    version only supports filtering for HEI's whose names _start_ with the given text string.

    """
    serializer_class = serializers.HigherEducationInstitutionSerializer
    queryset = HigherEducationInstitution.objects.all().order_by('name')
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )


class OrganizationalUnitViewSet(viewsets.ModelViewSet):
    """
    Organizational Unit List.

    **It's mandatory to provide an Organizational Unit UUID.**

    Dynamic Organizational Unit's name filter can be added with `q` parameter.
    """
    serializer_class = serializers.OrganizationalUnitSerializer
    queryset = OrganizationalUnit.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )

    def get_queryset(self):
        return self.queryset\
            .filter(id=self.kwargs["id"]) \
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


class OrganizationalUnitTreeViewSet(viewsets.ModelViewSet):
    """
    Organizational Unit List.

    **It's mandatory to provide an Higher Education Institution UUID.**

    Dynamic Organizational Unit's name filter can be added with `q` parameter.
    """
    serializer_class = serializers.NestedOrganizationalUnitSerializer
    queryset = HigherEducationInstitution.objects.all()

    def get_queryset(self):
        return self.queryset\
            .filter(id=self.kwargs["id"]) \
            .order_by('name')

    def get_serializer_context(self):
        """
        Add hei id to serializer context
        """
        if 'id' in self.kwargs:
            return {'id': self.kwargs["id"]}

        return {}
