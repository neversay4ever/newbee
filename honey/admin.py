from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import HoneyAll,HoneyCollection,HoneyCollector,HoneyComposition,HoneyTaxonomy

@admin.register(HoneyTaxonomy)
class HoneyTaxonomyAdmin(ImportExportModelAdmin):
    pass

@admin.register(HoneyComposition)
class HoneyCompositionAdmin(ImportExportModelAdmin):
    pass

@admin.register(HoneyCollector)
class HoneyCollectorAdmin(ImportExportModelAdmin):
    pass

@admin.register(HoneyCollection)
class HoneyCollectionAdmin(ImportExportModelAdmin):
    pass

@admin.register(HoneyAll)
class HoneyAllAdmin(ImportExportModelAdmin):
    pass