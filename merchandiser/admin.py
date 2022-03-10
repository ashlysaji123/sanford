from django.contrib import admin

from .models import Merchandiser, MerchandiserTarget, MerchandiserTask

admin.site.register(Merchandiser)
admin.site.register(MerchandiserTarget)
admin.site.register(MerchandiserTask)

# @admin.register(SalesExicutive)
# class SalesExicutiveAdmin(ImportExportActionModelAdmin):
#     list_display = ["__str__","user", "check_in","check_out", "is_deleted","location","late_reason","is_leave"]
#     list_filter = ["check_in","is_deleted"]
#     actions = [mark_deleted, mark_active]


# @admin.register(SalesExicutiveTarget)
# class SalesExicutiveTargetAdmin(ImportExportActionModelAdmin):
#     list_display = ["__str__","user", "start_date","end_date", "is_deleted","leave_reason","is_approved","is_rejected"]
#     list_filter = ["check_in","is_deleted"]
#     actions = [mark_deleted, mark_active]
