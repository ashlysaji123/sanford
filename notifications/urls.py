from django.urls import path, re_path

from . import views

app_name = "notifications"

urlpatterns = [
    path('create-notification', views.create_notification, name='create_notification'),
    path('notification-list', views.notification_list, name='notification_list'),
    re_path(r'^update-notification/(?P<pk>.*)/', views.update_notification ,name='update_notification'),
    re_path(r'^delete-notification/(?P<pk>.*)/', views.delete_notification, name='delete_notification'),
]
