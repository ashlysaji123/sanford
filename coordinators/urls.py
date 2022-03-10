from django.urls import path, re_path

from . import views

app_name = "coordinators"

urlpatterns = [
    # Manager
    path("create-manager", views.create_manager, name="create_manager"),
    path("manager-list", views.manager_list, name="manager_list"),
    re_path(
        r"^single-manager/(?P<pk>.*)/", views.manager_single, name="manager_single"
    ),
    re_path(
        r"^update-manager/(?P<pk>.*)/", views.update_manager, name="update_manager"
    ),
    re_path(
        r"^delete-manager/(?P<pk>.*)/", views.delete_manager, name="delete_manager"
    ),
    # Manager Task
    path("create-manager-task", views.create_manager_task, name="create_manager_task"),
    path("manager-task-list", views.manager_task_list, name="manager_task_list"),
    re_path(
        r"^update-manager-task/(?P<pk>.*)/",
        views.update_manager_task,
        name="update_manager_task",
    ),
    re_path(
        r"^delete-manager-task/(?P<pk>.*)/",
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
    re_path(
        r"^update-manager-target/(?P<pk>.*)/",
        views.update_manager_target,
        name="update_manager_target",
    ),
    re_path(
        r"^delete-manager-target/(?P<pk>.*)/",
        views.delete_manager_target,
        name="delete_manager_target",
    ),
    # Coordinator
    path("create-coordinator", views.create_coordinator, name="create_coordinator"),
    path("coordinator-list", views.coordinator_list, name="coordinator_list"),
    re_path(
        r"^single-coordinator/(?P<pk>.*)/",
        views.coordinator_single,
        name="coordinator_single",
    ),
    re_path(
        r"^update-coordinator/(?P<pk>.*)/",
        views.update_coordinator,
        name="update_coordinator",
    ),
    re_path(
        r"^delete-coordinator/(?P<pk>.*)/",
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
    re_path(
        r"^update-coordinator-task/(?P<pk>.*)/",
        views.update_coordinator_task,
        name="update_coordinator_task",
    ),
    re_path(
        r"^delete-coordinator-task/(?P<pk>.*)/",
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
    re_path(
        r"^update-coordinator-target/(?P<pk>.*)/",
        views.update_coordinator_target,
        name="update_coordinator_target",
    ),
    re_path(
        r"^delete-coordinator-target/(?P<pk>.*)/",
        views.delete_coordinator_target,
        name="delete_coordinator_target",
    ),
]
