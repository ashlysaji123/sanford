from django.urls import path

from . import views

app_name = "globalstaffs"

urlpatterns = [
    # Global Manager
    path("create/global-manager", views.create_global_manager, name="create_global_manager"),
    path("global-manager/list", views.global_manager_list, name="global_manager_list"),
    path("global-manager/single/<str:pk>/", views.global_manager_single, name="global_manager_single"),
    path("global-manager/update/<str:pk>/", views.update_global_manager, name="update_global_manager"),
    path("global-manager/delete/<str:pk>/", views.delete_global_manager, name="delete_global_manager"),
    # Global Manager Task
    path("create/global-manager/task", views.create_global_manager_task, name="create_global_manager_task"),
    path("global-manager/task/list", views.global_manager_task_list, name="global_manager_task_list"),
    path(
        "global-manager/task/update/<str:pk>/",
        views.update_global_manager_task,
        name="update_global_manager_task",
    ),
    path(
        "global-manager/task/delete/<str:pk>/",
        views.delete_global_manager_task,
        name="delete_global_manager_task",
    ),
    # Global Manager Target
    path(
        "global-manager/target/create",
        views.create_global_manager_target,
        name="create_global_manager_target",
    ),
    path("global-manager/target/list", views.global_manager_target_list, name="global_manager_target_list"),
    path(
        "global-manager/target/update/<str:pk>/",
        views.update_global_manager_target,
        name="update_global_manager_target",
    ),
    path(
        "global-manager/target/delete/<str:pk>/",
        views.delete_global_manager_target,
        name="delete_global_manager_target",
    ),
]
