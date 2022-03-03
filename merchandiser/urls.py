from django.urls import path,re_path
from . import views

app_name = "merchandiser"

urlpatterns = [
    # Merchandiser
    path('create-merchandiser', views.create_merchandiser, name='create_merchandiser'),
    path('merchandiser-list', views.merchandiser_list, name='merchandiser_list'),
    re_path(r'^single-merchandiser/(?P<pk>.*)/', views.merchandiser_single ,name='merchandiser_single'),
    re_path(r'^update-merchandiser/(?P<pk>.*)/', views.update_merchandiser ,name='update_merchandiser'),
    re_path(r'^delete-merchandiser/(?P<pk>.*)/', views.delete_merchandiser, name='delete_merchandiser'),
    # Merchandiser Task
    path('create-merchandiser-task', views.create_merchandiser_task, name='create_merchandiser_task'),
    path('merchandiser-task-list', views.merchandiser_task_list, name='merchandiser_task_list'),
    re_path(r'^update-merchandiser-task/(?P<pk>.*)/', views.update_merchandiser_task ,name='update_merchandiser_task'),
    re_path(r'^delete-merchandiser-task/(?P<pk>.*)/', views.delete_merchandiser_task, name='delete_merchandiser_task'),
    # Merchandiser Target
    path('create-merchandiser-target', views.create_merchandiser_target, name='create_merchandiser_target'),
    path('merchandiser-target-list', views.merchandiser_target_list, name='merchandiser_target_list'),
    re_path(r'^update-merchandiser-target/(?P<pk>.*)/', views.update_merchandiser_target ,name='update_merchandiser_target'),
    re_path(r'^delete-merchandiser-target/(?P<pk>.*)/', views.delete_merchandiser_target, name='delete_merchandiser_target'),
    
]
