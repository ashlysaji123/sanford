from django.urls import path,re_path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination
from sales.models import OpeningStock

from . import views
from .serializers import OpeningStockSerializer

app_name = "sales"

urlpatterns = [
    # path(
    #     "targets/",
    #     ListAPIView.as_view(
    #         queryset=Target.objects.filter(is_deleted=False),
    #         serializer_class=TargetSerializer,
    #         pagination_class=StandardResultsSetPagination,
    #         permission_classes =[IsAuthenticated],
    #     ),
    # ),
    # path(
    #     "targets/view/<str:pk>/",
    #     RetrieveAPIView.as_view(
    #         queryset=Target.objects.filter(is_deleted=False),
    #         serializer_class=TargetSerializer,
    #         permission_classes =[IsAuthenticated],
    #     ),
    # ),
    # path("mytarget/", views.MyTarget.as_view()),
    path(
        "opening_stocks/",
        ListAPIView.as_view(
            queryset=OpeningStock.objects.filter(is_deleted=False),
            serializer_class=OpeningStockSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "opening_stocks/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=OpeningStock.objects.filter(is_deleted=False),
            serializer_class=OpeningStockSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),

    path("create-sales/", views.create_sales),
    path("update-sales/", views.update_sale),
    re_path(r'^update-sales/(?P<pk>.*)/', views.update_sale),
    path("my-sales/", views.my_sales),
]
