from rest_framework import serializers
from core.models import HigherEducationInstitution, LearningOpportunitySpecification, OrganizationalUnit


class HigherEducationInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = HigherEducationInstitution
        fields = '__all__'


class OrganizationalUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationalUnit
        fields = '__all__'


class LearningOpportunitySpecificationSerializer(serializers.ModelSerializer):
    organizational_unit = OrganizationalUnitSerializer()

    class Meta:
        model = LearningOpportunitySpecification
        fields = '__all__'
