from django.urls import path
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny

from core.pagination import StandardResultsSetPagination
from votings.models import Voting,VotingItem
from .serializers import (
    VotingItemSerializer,
    VotingSerializer
)

import datetime

today = datetime.date.today()
from api.v1.votings import views

app_name = "votings"

urlpatterns = [
    path(
        "voting/items/",
        ListAPIView.as_view(
            queryset=VotingItem.objects.filter(voting_enddate__gte=today),
            serializer_class=VotingItemSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[AllowAny],
        ),
    ),
     path(
         "voting/view/<str:pk>/",views.create_voting),
    
]
