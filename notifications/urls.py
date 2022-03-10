from django.urls import path

from . import views

app_name = "notifications"

urlpatterns = [
    path("create-notification", views.create_notification, name="create_notification"),
    path("notification-list", views.notification_list, name="notification_list"),
    path(
        "update-notification/<str:pk>/",
        views.update_notification,
        name="update_notification",
    ),
    path(
        "delete-notification/<str:pk>/",
        views.delete_notification,
        name="delete_notification",
    ),
]
