from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import Country, Language, Region, State, Year
from core.pagination import StandardResultsSetPagination

from .serializers import (CountrySerializer, LanguageSerializer,
                          RegionSerializer, StateSerializer, YearSerializer)

app_name = "core"

urlpatterns = [
    path(
        "countries/",
        ListAPIView.as_view(
            queryset=Country.objects.filter(is_deleted=False),
            serializer_class=CountrySerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "states/",
        ListAPIView.as_view(
            queryset=State.objects.filter(is_deleted=False),
            serializer_class=StateSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "regions/",
        ListAPIView.as_view(
            queryset=Region.objects.filter(is_deleted=False),
            serializer_class=RegionSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "languages/",
        ListAPIView.as_view(
            queryset=Language.objects.filter(is_deleted=False),
            serializer_class=LanguageSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "years/",
        ListAPIView.as_view(
            queryset=Year.objects.filter(is_deleted=False),
            serializer_class=YearSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "countries/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Country.objects.filter(is_deleted=False),
            serializer_class=CountrySerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "states/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=State.objects.filter(is_deleted=False),
            serializer_class=StateSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "regions/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Region.objects.filter(is_deleted=False),
            serializer_class=RegionSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "languages/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Language.objects.filter(is_deleted=False),
            serializer_class=LanguageSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "years/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Year.objects.filter(is_deleted=False),
            serializer_class=YearSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
]
