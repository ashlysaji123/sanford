from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path("DAR-tasks/",views.DAR_task),
    path("DAR-list/",views.DAR_list),
    path("create/collect-money/",views.create_collect_money),
    path("create-order/<str:pk>/",views.create_order),
    path("upload-photo/<str:pk>/",views.create_upload_photo),
]