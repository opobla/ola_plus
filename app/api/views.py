from rest_framework import viewsets, filters
import django_filters
from rest_framework.permissions import IsAuthenticated

from . import serializers
from core.models import HigherEducationInstitution, LearningOpportunitySpecification, OrganizationalUnit
from rest_framework.response import Response

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

    def get_permissions(self):
        if self.request.method == 'GET':
            pass
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super(viewsets.ModelViewSet, self).get_permissions()


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

    def get_permissions(self):
        if self.request.method == 'GET':
            pass
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super(viewsets.ModelViewSet, self).get_permissions()

    def delete_los_from_ounit(self, ounit_id):
        return Response("lolo", 200)

    def destroy(self, request, id=None):
        query = self.queryset.filter(id=id)
        query.delete()
        return Response()


class OrganizationalUnitLos(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]

    def delete_los_from_ounit(self, request, ounit_id=None, *args, **kwargs):
        LearningOpportunitySpecification.objects.filter(
            organizational_unit="b3e24a6f-2b2e-4fd7-a500-c4570d2778b7").delete()
        return Response("LOS for {} deleted".format(ounit_id), 200)

class LosFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.rest_framework.CharFilter(field_name='title', lookup_expr='icontains')
    isced_code = django_filters.rest_framework.NumberFilter(field_name='isced_code', lookup_expr='startswith')
    academic_term = django_filters.rest_framework.CharFilter(name='academic_term', lookup_expr='iexact')
    start_date_before = django_filters.rest_framework.DateFilter(name='start_date', lookup_expr='lte')
    start_date_after = django_filters.rest_framework.DateFilter(name='start_date', lookup_expr='gte')
    end_date_before = django_filters.rest_framework.DateFilter(name='end_date', lookup_expr='lte')
    end_date_after = django_filters.rest_framework.DateFilter(name='end_date', lookup_expr='gte')

    class Meta:
        model = LearningOpportunitySpecification
        fields = ['title', 'isced_code', 'credit_value', 'academic_term', 'start_date_before', 'start_date_after',
                  'end_date_before', 'end_date_after']


class LearningOpportunitySpecificationModelViewSet(viewsets.ModelViewSet):
    """
    Learning Opportunity Specification List.

    **It's mandatory to provide an Organizational Unit UUID.**

    Dynamic Learning Opportunity Specification's title filter can be added with `q` parameter.
    """
    serializer_class = serializers.LearningOpportunitySpecificationSerializer
    queryset = LearningOpportunitySpecification.objects.all().order_by('title')
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = LosFilter

    def get_queryset(self):
        return self.queryset \
            .filter(organizational_unit_id=self.kwargs["id"]) \
            .order_by('title')

    def get_permissions(self):
        if self.request.method == 'GET':
            pass
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super(viewsets.ModelViewSet, self).get_permissions()


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

    def destroy(self, request, id=None):
        query = self.queryset.filter(id=id)
        query.delete()
        return Response()

    def get_serializer_context(self):
        """
        Add hei id to serializer context
        """
        if 'id' in self.kwargs:
            return {'id': self.kwargs["id"]}

        return {}

    def get_permissions(self):
        if self.request.method == 'GET':
            pass
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super(viewsets.ModelViewSet, self).get_permissions()


class LosFiltersViewSet(viewsets.ViewSet):
    queryset = LearningOpportunitySpecification.objects.all()

    serializer_class = serializers.LearningOpportunitySpecificationDistinctSerializer

    def list(self, request):
        academic_term = LearningOpportunitySpecification.objects.values_list('academic_term', flat=True) \
                                                                .order_by('academic_term').distinct()
        credit_value = LearningOpportunitySpecification.objects.values_list('credit_value', flat=True) \
                                                               .order_by('credit_value').distinct()

        return Response({'academic_term': list(academic_term), 'credit_value': list(credit_value)})
