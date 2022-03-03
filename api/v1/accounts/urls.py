from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

app_name = "accounts"

urlpatterns = [
    path("user/<str:pk>/", views.UserProfileView.as_view(), name="user_profile"),
    path("login/", views.MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", views.MyProfileView.as_view(), name="profile"),
    path(
        "change_password/<str:pk>/",
        views.ChangePasswordView.as_view(),
        name="auth_change_password",
    ),
]
