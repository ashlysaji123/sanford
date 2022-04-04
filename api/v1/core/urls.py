from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import SubRegion, Language, Region, Area, Year,LocalArea
from core.pagination import StandardResultsSetPagination

from .serializers import (
    SubRegionSerializer,
    LanguageSerializer,
    RegionSerializer,
    AreaSerializer,
    YearSerializer,
    LocalAreaSerializer
)

app_name = "core"

urlpatterns = [
    path(
        "sub-regions/",
        ListAPIView.as_view(
            queryset=SubRegion.objects.filter(is_deleted=False),
            serializer_class=SubRegionSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "area-list/",
        ListAPIView.as_view(
            queryset=Area.objects.filter(is_deleted=False),
            serializer_class=AreaSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "local-area-list/",
        ListAPIView.as_view(
            queryset=LocalArea.objects.filter(is_deleted=False),
            serializer_class=LocalAreaSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "regions/",
        ListAPIView.as_view(
            queryset=Region.objects.filter(is_deleted=False),
            serializer_class=RegionSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "languages/",
        ListAPIView.as_view(
            queryset=Language.objects.filter(is_deleted=False),
            serializer_class=LanguageSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "years/",
        ListAPIView.as_view(
            queryset=Year.objects.filter(is_deleted=False),
            serializer_class=YearSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "sub-region/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=SubRegion.objects.filter(is_deleted=False),
            serializer_class=SubRegionSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "area/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Area.objects.filter(is_deleted=False),
            serializer_class=AreaSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "local-area/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=LocalArea.objects.filter(is_deleted=False),
            serializer_class=LocalAreaSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "regions/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Region.objects.filter(is_deleted=False),
            serializer_class=RegionSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "languages/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Language.objects.filter(is_deleted=False),
            serializer_class=LanguageSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "years/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Year.objects.filter(is_deleted=False),
            serializer_class=YearSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
]
