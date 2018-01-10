from django.contrib import admin
from . import models


admin.site.site_header = 'OLA+ Admin'
admin.site.site_title = 'OLA+ Admin'
admin.site.index_title = 'OLA+ Admin'


class OrganizationalUnitInLineAdmin(admin.TabularInline):
    ordering = ['name']
    search_fields = ['name']
    autocomplete_fields = ['parent', 'higher_education_institution']
    model = models.OrganizationalUnit
    min_num = 1


class HigherEducationInstitutionAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    autocomplete_fields = ['origin']
    inlines = [OrganizationalUnitInLineAdmin, ]


class HigherEducationInstitutionOriginAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class OrganizationalUnitAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    autocomplete_fields = ['parent', 'higher_education_institution']


class LearningOpportunitySpecificationAdmin(admin.ModelAdmin):
    ordering = ['title']
    search_fields = ['title']
    autocomplete_fields = ['organizational_unit']


admin.site.register(models.HigherEducationInstitution, HigherEducationInstitutionAdmin)
admin.site.register(models.HigherEducationInstitutionOrigin, HigherEducationInstitutionOriginAdmin)
admin.site.register(models.OrganizationalUnit, OrganizationalUnitAdmin)
admin.site.register(models.LearningOpportunitySpecification, LearningOpportunitySpecificationAdmin)
