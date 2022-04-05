from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "staffs"

urlpatterns = [
    # staffs
    path("staffs/", login_required(views.StaffList.as_view()), name="staff_list"),
    path("view/staff/<str:pk>/", login_required(views.StaffDetail.as_view()), name="view_staff",),
]