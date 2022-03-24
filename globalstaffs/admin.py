from django.contrib import admin

from .models import (
    GlobalManager,
    GlobalManagerTarget,
    GlobalManagerTask
)

admin.site.register(GlobalManager)
admin.site.register(GlobalManagerTarget)
admin.site.register(GlobalManagerTask)
