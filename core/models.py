from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class HigherEducationInstitutionOrigin(BaseModel):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class HigherEducationInstitution(BaseModel):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    origin = models.ForeignKey(HigherEducationInstitutionOrigin, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class OrganizationalUnit(BaseModel):

    name = models.CharField(max_length=255)
    higher_education_institution = models.ForeignKey(HigherEducationInstitution, on_delete=models.DO_NOTHING)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class LearningOpportunitySpecification(BaseModel):

    organizational_unit = models.ForeignKey(OrganizationalUnit, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=255)
    area = models.CharField(max_length=255, blank=True, null=True)
    isced_code = models.CharField(max_length=255, blank=True, null=True)
    credit_scheme = models.CharField(max_length=255, blank=True, null=True)
    credit_level = models.CharField(max_length=255, blank=True, null=True)
    credit_value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
