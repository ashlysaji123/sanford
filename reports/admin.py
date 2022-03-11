from django.contrib import admin
from reports.models import DARNotes,DARTask,DARReschedule
# Register your models here.

admin.site.register(DARNotes)
admin.site.register(DARTask)
admin.site.register(DARReschedule)