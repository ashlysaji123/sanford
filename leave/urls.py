from django.urls import path,re_path
from . import views

app_name = "leave"

urlpatterns = [
    #leave
    path('leave-request-list', views.leave_request_list, name='leave_request_list'),
    path('approved-leave-list', views.approved_leave_list, name='approved_leave_list'),
    re_path(r'^single-leave/(?P<pk>.*)/', views.leave_single ,name='leave_single'),
    
]
