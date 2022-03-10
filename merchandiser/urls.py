from django.urls import path

from . import views

app_name = "merchandiser"

urlpatterns = [
    # Merchandiser
    path("create-merchandiser", views.create_merchandiser, name="create_merchandiser"),
    path("merchandiser-list", views.merchandiser_list, name="merchandiser_list"),
    path(
        "single-merchandiser/<str:pk>/",
        views.merchandiser_single,
        name="merchandiser_single",
    ),
    path(
        "update-merchandiser/<str:pk>/",
        views.update_merchandiser,
        name="update_merchandiser",
    ),
    path(
        "delete-merchandiser/<str:pk>/",
        views.delete_merchandiser,
        name="delete_merchandiser",
    ),
    # Merchandiser Task
    path(
        "create-merchandiser-task",
        views.create_merchandiser_task,
        name="create_merchandiser_task",
    ),
    path(
        "merchandiser-task-list",
        views.merchandiser_task_list,
        name="merchandiser_task_list",
    ),
    path(
        "update-merchandiser-task/<str:pk>/",
        views.update_merchandiser_task,
        name="update_merchandiser_task",
    ),
    path(
        "delete-merchandiser-task/<str:pk>/",
        views.delete_merchandiser_task,
        name="delete_merchandiser_task",
    ),
    # Merchandiser Target
    path(
        "create-merchandiser-target",
        views.create_merchandiser_target,
        name="create_merchandiser_target",
    ),
    path(
        "merchandiser-target-list",
        views.merchandiser_target_list,
        name="merchandiser_target_list",
    ),
    path(
        "update-merchandiser-target/<str:pk>/",
        views.update_merchandiser_target,
        name="update_merchandiser_target",
    ),
    path(
        "delete-merchandiser-target/<str:pk>/",
        views.delete_merchandiser_target,
        name="delete_merchandiser_target",
    ),
]
