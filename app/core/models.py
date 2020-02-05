from django.db import models
from django.core.exceptions import ValidationError
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class HigherEducationInstitution(BaseModel):

    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class OrganizationalUnit(BaseModel):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, default=None)
    higher_education_institution = models.ForeignKey(HigherEducationInstitution, on_delete=models.CASCADE, related_name='ounits')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='ounits')

    def validate_unique(self, exclude=None):
        qs = OrganizationalUnit.objects.filter(code=self.code)
        if qs.filter(parent=self.parent, higher_education_institution=self.higher_education_institution).exists():
            raise ValidationError('Organizational unit with same higher_education_institution, parent and code is not allowed')

    def save(self, *args, **kwargs):
        self.validate_unique()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class LearningOpportunitySpecification(BaseModel):

    organizational_unit = models.ForeignKey(OrganizationalUnit, on_delete=models.CASCADE, null=True, blank=True, related_name='los')
    code = models.CharField(max_length=255, default=None)
    title = models.CharField(max_length=255)
    area = models.CharField(max_length=255, blank=True, null=True)
    isced_code = models.CharField(max_length=255, blank=True, null=True)
    credit_scheme = models.CharField(max_length=255, blank=True, null=True)
    credit_level = models.CharField(max_length=255, blank=True, null=True)
    credit_value = models.CharField(max_length=255, blank=True, null=True)
    academic_term = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, blank=True, null=True)

    class Meta:
        unique_together = ('organizational_unit', 'code')

    def __str__(self):
        return self.title
