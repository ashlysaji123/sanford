from django.urls import path,re_path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination
from api.v1.accounts.serializers import UserSerializer
from accounts.models import User
from merchandiser.models import Merchandiser
from .serializers import MerchandiserSerializer
from . import views

app_name = "merchandiser"

urlpatterns = [
    path(
        "",
        ListAPIView.as_view(
            queryset=Merchandiser.objects.filter(is_deleted=False),
            serializer_class=MerchandiserSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Merchandiser.objects.filter(is_deleted=False),
            serializer_class=MerchandiserSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path("merchandiser-target/", views.merchandiser_target),
    path("merchandiser-tasks/", views.merchandiser_task),
    re_path(r'^merchandiser-mark-tasks/(?P<pk>.*)/', views.merchandiser_mark_task),
    path("merchandiser-completed-tasks/", views.merchandiser_completed_task),
    path("merchandiser-profile/", views.merchandiser_profile),
    path("merchandiser-sale-status/", views.merchandiser_sale_status),

]
