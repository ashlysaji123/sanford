from django.urls import path
from django.contrib.auth.decorators import login_required

from reports import views

app_name = "reports"


urlpatterns = [
    #DAR 
    path("create-DAR", views.create_DAR, name="create_DAR"),
    path("DAR-list", views.DAR_list, name="DAR_list"),
    path("single-DAR/<str:pk>/", views.DAR_single, name="DAR_single"),
    path("update-DAR/<str:pk>/", views.update_DAR, name="update_DAR"),
    path("delete-DAR/<str:pk>/", views.delete_DAR, name="delete_DAR"),
    #DAR Reschedule
    path("DAR/reschedule/list/", login_required(views.DARRescheduleList.as_view()), name="DAR_reschedule_list"),
    path("DAR/reschedule/accepted-list/", login_required(views.DARAcceptedList.as_view()), name="DAR_accepted_list"),
    path("accept-reschedule/<str:pk>/", views.accept_reschedule, name="accept_reschedule"),
    path("reject-reschedule/<str:pk>/", views.reject_reschedule, name="reject_reschedule"),
    #DMR 
    path("DMR-list/", views.DMRList, name="DMR_list"),
]
