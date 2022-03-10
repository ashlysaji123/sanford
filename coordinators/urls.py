from django.urls import path

from . import views

app_name = "coordinators"

urlpatterns = [
    # Manager
    path("create-manager", views.create_manager, name="create_manager"),
    path("manager-list", views.manager_list, name="manager_list"),
    path("single-manager/<str:pk>/", views.manager_single, name="manager_single"),
    path("update-manager/<str:pk>/", views.update_manager, name="update_manager"),
    path("delete-manager/<str:pk>/", views.delete_manager, name="delete_manager"),
    # Manager Task
    path("create-manager-task", views.create_manager_task, name="create_manager_task"),
    path("manager-task-list", views.manager_task_list, name="manager_task_list"),
    path(
        "update-manager-task/<str:pk>/",
        views.update_manager_task,
        name="update_manager_task",
    ),
    path(
        "delete-manager-task/<str:pk>/",
        views.delete_manager_task,
        name="delete_manager_task",
    ),
    # Manager Target
    path(
        "create-manager-target",
        views.create_manager_target,
        name="create_manager_target",
    ),
    path("manager-target-list", views.manager_target_list, name="manager_target_list"),
    path(
        "update-manager-target/<str:pk>/",
        views.update_manager_target,
        name="update_manager_target",
    ),
    path(
        "delete-manager-target/<str:pk>/",
        views.delete_manager_target,
        name="delete_manager_target",
    ),
    # Coordinator
    path("create-coordinator", views.create_coordinator, name="create_coordinator"),
    path("coordinator-list", views.coordinator_list, name="coordinator_list"),
    path(
        "single-coordinator/<str:pk>/",
        views.coordinator_single,
        name="coordinator_single",
    ),
    path(
        "update-coordinator/<str:pk>/",
        views.update_coordinator,
        name="update_coordinator",
    ),
    path(
        "delete-coordinator/<str:pk>/",
        views.delete_coordinator,
        name="delete_coordinator",
    ),
    # Coordinator Task
    path(
        "create-coordinator-task",
        views.create_coordinator_task,
        name="create_coordinator_task",
    ),
    path(
        "coordinator-task-list",
        views.coordinator_task_list,
        name="coordinator_task_list",
    ),
    path(
        "update-coordinator-task/<str:pk>/",
        views.update_coordinator_task,
        name="update_coordinator_task",
    ),
    path(
        "delete-coordinator-task/<str:pk>/",
        views.delete_coordinator_task,
        name="delete_coordinator_task",
    ),
    # Coordinator Target
    path(
        "create-coordinator-target",
        views.create_coordinator_target,
        name="create_coordinator_target",
    ),
    path(
        "coordinator-target-list",
        views.coordinator_target_list,
        name="coordinator_target_list",
    ),
    path(
        "update-coordinator-target/<str:pk>/",
        views.update_coordinator_target,
        name="update_coordinator_target",
    ),
    path(
        "delete-coordinator-target/<str:pk>/",
        views.delete_coordinator_target,
        name="delete_coordinator_target",
    ),
]
