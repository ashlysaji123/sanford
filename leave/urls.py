from django.urls import path

from . import views

app_name = "leave"

urlpatterns = [
    # leave
    path("pending/leave-requests", views.leave_request_list, name="leave_request_list"),
    path("leave/approved/list", views.approved_leave_list, name="approved_leave_list"),
    path("leave/rejected/list", views.rejected_leave_list, name="rejected_leave_list"),
    path("single-leave/<str:pk>/", views.leave_single, name="leave_single"),
    path("accept-leave/<str:pk>/", views.accept_leave, name="accept_leave"),
    path("reject-leave/<str:pk>/", views.reject_leave, name="reject_leave"),
]
