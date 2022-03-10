from django.urls import path,re_path
from reports import views

app_name = "reports"

urlpatterns = [
    path('create-DAR', views.create_DAR, name='create_DAR'),
    path('DAR-list', views.DAR_list, name='DAR_list'),
    re_path(r'^single-DAR/(?P<pk>.*)/', views.DAR_single ,name='DAR_single'),
    re_path(r'^update-DAR/(?P<pk>.*)/', views.update_DAR ,name='update_DAR'),
    re_path(r'^delete-DAR/(?P<pk>.*)/', views.delete_DAR, name='delete_DAR'),
    
]
