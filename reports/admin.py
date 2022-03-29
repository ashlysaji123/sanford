from django.contrib import admin
from reports.models import DARNotes,DARTask,DARReschedule,CollectMoney,Order,OrderItem,UploadPhoto
# Register your models here.

admin.site.register(DARNotes)
admin.site.register(DARTask)
admin.site.register(DARReschedule)
admin.site.register(CollectMoney)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UploadPhoto)
