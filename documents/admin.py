from django.contrib import admin

from documents.models import EmployeeDocuments, EmployeeDocumentsItems

# Register your models here.
@admin.register(EmployeeDocuments)
class VotingItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_approved', 'is_rejected']

@admin.register(EmployeeDocumentsItems)
class VotingAdmin(admin.ModelAdmin):
    list_display = ['title','image']

# Register your models here.
