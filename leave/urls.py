from django.urls import path,re_path
from . import views

app_name = "leave"

urlpatterns = [
    #leave
    path('leave-request-list', views.leave_request_list, name='leave_request_list'),
    path('approved-leave-list', views.approved_leave_list, name='approved_leave_list'),
    re_path(r'^single-leave/(?P<pk>.*)/', views.leave_single ,name='leave_single'),
    re_path(r'^accept-leave/(?P<pk>.*)/', views.accept_leave ,name='accept_leave'),
    re_path(r'^reject-leave/(?P<pk>.*)/', views.reject_leave ,name='reject_leave'),
    
]
