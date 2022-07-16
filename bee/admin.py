from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import CollectionData,Taxonomy, SpecimenDetails,HeadthoraxStorage, AbdomenStorage,GutStorage,LegStorage, BeeAll

@admin.register(CollectionData)
class CollectionDataAdmin(ImportExportModelAdmin):
    search_fields = ['exact_site']

@admin.register(Taxonomy)
class TaxonomyAdmin(ImportExportModelAdmin):
    search_fields = ['sample_breed']

@admin.register(SpecimenDetails)
class SpecimenDetailsAdmin(ImportExportModelAdmin):
    search_fields = ['sample_id']

@admin.register(HeadthoraxStorage)
class HeadthoraxStorageAdmin(ImportExportModelAdmin):
    search_fields = ['headthorax_preservation']

@admin.register(AbdomenStorage)
class AbdomenStorageAdmin(ImportExportModelAdmin):
    search_fields = ['abdomen_preservation']

@admin.register(GutStorage)
class GutStorageAdmin(ImportExportModelAdmin):
    search_fields = ['gut_preservation']

@admin.register(LegStorage)
class LegStorageAdmin(ImportExportModelAdmin):
    search_fields = ['leg_preservation']

@admin.register(BeeAll)
class BeeAllAdmin(ImportExportModelAdmin):
    search_fields = ['sample_id']