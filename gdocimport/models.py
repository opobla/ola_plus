from django.db import models

# Create your models here.


class HigherEducationInstitutes(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        verbose_name = 'HEI'
        verbose_name_plural = 'HEIS'

    def __str__(self):
        return self.name


class OrganizationUnit(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    parent_ounit = models.IntegerField()
    subject = models.ForeignKey()

    class Meta:
        verbose_name = 'OUNIT'
        verbose_name_plural = 'OUNITS'

    def __str__(self):
        return self.name


class Subject(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    isced_code = models.IntegerField()
    credit_scheme = models.IntegerField()
    credit_level = models.CharField(max_length=200)
    credit_value = models.IntegerField()

    class Meta:
        verbose_name = 'LOS'
        verbose_name_plural = 'SUBJECTS'

    def __str__(self):
        return self.name