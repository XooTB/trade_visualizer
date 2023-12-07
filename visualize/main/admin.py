from django.contrib import admin
from .models import data
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.


class dataResource(resources.ModelResource):
    class Meta:
        model = data

class dataAdmin(ImportExportModelAdmin):
    """
    Admin class for managing data.
    """
    list_display = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']
    search_fields = ['trade_code']
    resource_class = dataResource
    list_per_page = 1000


admin.site.register(data, dataAdmin)

