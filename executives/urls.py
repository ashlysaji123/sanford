from django.urls import path

from . import views

app_name = "executives"

urlpatterns = [
    # Supervisor
    path("supervisor/create", views.create_supervisor, name="create_supervisor"),
    path("supervisor/list", views.supervisor_list, name="supervisor_list"),
    path(
        "supervisor/single/<str:pk>/",
        views.supervisor_single,
        name="supervisor_single",
    ),
    path(
        "supervisor/update/<str:pk>/",
        views.update_supervisor,
        name="update_supervisor",
    ),
    path(
        "supervisor/delete/<str:pk>/",
        views.delete_supervisor,
        name="delete_supervisor",
    ),
    # Supervisor Task
    path(
        "supervisor/task/create",
        views.create_supervisor_task,
        name="create_supervisor_task",
    ),
    path("supervisor/task/list", views.supervisor_task_list, name="supervisor_task_list"),
    path(
        "supervisor/task/update/<str:pk>/",
        views.update_supervisor_task,
        name="update_supervisor_task",
    ),
    path(
        "supervisor/task/delete/<str:pk>/",
        views.delete_supervisor_task,
        name="delete_supervisor_task",
    ),
    # Supervisor Target
    path(
        "supervisor/target/create",
        views.create_supervisor_target,
        name="create_supervisor_target",
    ),
    path(
        "supervisor/target/list",
        views.supervisor_target_list,
        name="supervisor_target_list",
    ),
    path(
        "supervisor/target/update/<str:pk>/",
        views.update_supervisor_target,
        name="update_supervisor_target",
    ),
    path(
        "supervisor/target/delete/<str:pk>/",
        views.delete_supervisor_target,
        name="delete_supervisor_target",
    ),
    # Executive
    path("create-executive", views.create_executive, name="create_executive"),
    path("executive-list", views.executive_list, name="executive_list"),
    path(
        "single-executive/<str:pk>/",
        views.executive_single,
        name="executive_single",
    ),
    path(
        "update-executive/<str:pk>/",
        views.update_executive,
        name="update_executive",
    ),
    path(
        "delete-executive/<str:pk>/",
        views.delete_executive,
        name="delete_executive",
    ),
    # Executive Task
    path(
        "create-executive-task",
        views.create_executive_task,
        name="create_executive_task",
    ),
    path("executive-task-list", views.executive_task_list, name="executive_task_list"),
    path(
        "update-executive-task/<str:pk>/",
        views.update_executive_task,
        name="update_executive_task",
    ),
    path(
        "delete-executive-task/<str:pk>/",
        views.delete_executive_task,
        name="delete_executive_task",
    ),
    # Executive Target
    path(
        "create-executive-target",
        views.create_executive_target,
        name="create_executive_target",
    ),
    path(
        "executive-target-list",
        views.executive_target_list,
        name="executive_target_list",
    ),
    path(
        "update-executive-target/<str:pk>/",
        views.update_executive_target,
        name="update_executive_target",
    ),
    path(
        "delete-executive-target/<str:pk>/",
        views.delete_executive_target,
        name="delete_executive_target",
    ),
]
