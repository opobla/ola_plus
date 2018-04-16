from rest_framework import serializers
from core.models import HigherEducationInstitution, LearningOpportunitySpecification, OrganizationalUnit


class HigherEducationInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = HigherEducationInstitution
        fields = '__all__'


class LearningOpportunitySpecificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningOpportunitySpecification
        fields = '__all__'


class RecursiveField(serializers.ModelSerializer):
    los = LearningOpportunitySpecificationSerializer(many=True, read_only=True, required=False)

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

    def to_internal_value(self, data):
        serializer = self.parent.parent.__class__(context=self.context)
        return serializer.to_internal_value(data)

    class Meta:
        model = OrganizationalUnit
        fields = [
                'id',
                'name',
                'code',
                'ounits',
                'los']
        depth = 1


class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        if isinstance(data, list):
            return super(FilteredListSerializer, self).to_representation(data)

        data = data.filter(parent=None)
        return super(FilteredListSerializer, self).to_representation(data)


class OrganizationalUnitSerializer(serializers.ModelSerializer):
    los = LearningOpportunitySpecificationSerializer(many=True, read_only=True, required=False)
    ounits = RecursiveField(many=True, read_only=False, required=False)
    higher_education_institution = serializers.PrimaryKeyRelatedField(required=False,
                                                                      queryset=HigherEducationInstitution.objects.all())
    parent = serializers.PrimaryKeyRelatedField(required=False, queryset=OrganizationalUnit.objects.all())

    class Meta:
        model = OrganizationalUnit
        list_serializer_class = FilteredListSerializer
        fields = [
                'id',
                'name',
                'code',
                'higher_education_institution',
                'parent',
                'los',
                'ounits']
        read_only_fields = ('higher_education_institution', 'parent',)
        depth = 1

    def create(self, validated_data):
        subounits = []
        if 'ounits' in validated_data:
            subounits = validated_data.pop('ounits')

        hei_id = self.context['id']

        ounit = OrganizationalUnit.objects.create(higher_education_institution_id=hei_id,
                                                  **validated_data)

        for subounit in subounits:
            subounit = OrganizationalUnit.objects.create(parent=ounit,
                                                         higher_education_institution_id=hei_id,
                                                         **subounit)

        return ounit


class NestedOrganizationalUnitSerializer(serializers.ModelSerializer):
    ounits = OrganizationalUnitSerializer(many=True, read_only=False, required=True)

    class Meta(object):
        model = HigherEducationInstitution
        fields = ['ounits',
                  'name',
                  'email']
        read_only_fields = ('name', 'email')

    def create(self, validated_data):
        hei = None
        hei_id = None

        if 'id' in self.context:
            hei_id = self.context['id']
            hei = HigherEducationInstitution.objects.get(pk=hei_id)
        else:
            ounits = validated_data['ounits']
            hei = ounits[0]['higher_education_institution']
            hei_id = hei.id

        new_ounits = validated_data.pop('ounits')

        parent_ounit = None
        for new_ounit in new_ounits:
            subounits = []
            if 'ounits' in new_ounit:
                subounits = new_ounit.pop('ounits')

            parent_ounit = hei.ounits.create(**new_ounit)

            for subounit in subounits:
                subounit['higher_education_institution'] = hei_id
                subounit['parent'] = parent_ounit.id

            if subounits:
                ounit_serializer = NestedOrganizationalUnitSerializer(data={'ounits': subounits})
                if ounit_serializer.is_valid():
                    ounit_serializer.save()

        return hei


class LearningOpportunitySpecificationDistinctSerializer(serializers.ModelSerializer):
    academic_term = serializers.ListField()
    credit_value = serializers.ListField()

    class Meta(object):
        model = LearningOpportunitySpecification
        fields = ['academic_term', 'credit_value']
