from django.urls import path

from reports import views

app_name = "reports"

urlpatterns = [
    path("create-DAR", views.create_DAR, name="create_DAR"),
    path("DAR-list", views.DAR_list, name="DAR_list"),
    path("single-DAR/<str:pk>/", views.DAR_single, name="DAR_single"),
    path("update-DAR/<str:pk>/", views.update_DAR, name="update_DAR"),
    path("delete-DAR/<str:pk>/", views.delete_DAR, name="delete_DAR"),
]
