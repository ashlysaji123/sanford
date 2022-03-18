import datetime
from inspect import formatannotation

from django.db.models import Avg
from django.http import Http404
from django.shortcuts import get_object_or_404
from api.v1 import executives
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from executives.models import SalesExecutive,SalesExecutiveTarget,SalesExecutiveTask

from .serializers import (
    SalesExecutiveTargetSerializer,
    SalesExecutiveTaskSerializer,
    SalesExecutiveProfileSerializer
)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salesexecutive_target(request):
    """
    Fetch target based on which user is requesting
    for target and current year and month
    """
    user = request.user
    executive = get_object_or_404(SalesExecutive, user=user)
    try:
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        target = SalesExecutiveTarget.objects.filter(
            user=executive, year=current_year, month=current_month
        )
        serializer = SalesExecutiveTargetSerializer(
            target, many=True, context={"request": request}
        )
        return Response(serializer.data)
    except SalesExecutiveTarget.DoesNotExist:
        target = None
        response_data = {
            "status": False,
            "detail": "No Target Assigned",
        }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salesexecutive_task(request):
    """
    Fetch not completed task based on which user is requesting
    for task
    """
    user = request.user
    executive = get_object_or_404(SalesExecutive, user=user)
    task = SalesExecutiveTask.objects.filter(user=executive, is_completed=False)
    serializer = SalesExecutiveTaskSerializer(
        task, many=True, context={"request": request}
    )
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salesexecutive_completed_task(request):
    """
    Fetch completed task based on which user is requesting
    for task
    """
    user = request.user
    executive = get_object_or_404(SalesExecutive, user=user)
    task = SalesExecutiveTask.objects.filter(user=executive, is_completed=True)
    serializer = SalesExecutiveTaskSerializer(
        task, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def salesexecutive_mark_task(request, pk):
    """
    Marking task as a Completed task
    """
    try:
        task = SalesExecutiveTask.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        response = {
            "status": 200,
            "message": "Successfully Updated.",
        }
        return Response(response, status=status.HTTP_201_CREATED)
    except SalesExecutiveTask.DoesNotExist:
        raise Http404


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salesexecutive_profile(request):
    try:
        user = request.user
        queryset = SalesExecutive.objects.get(user=user)
    except:
        response = "User not found"
        return Response(response, status=status.HTTP_200_OK)
    
    serializer = SalesExecutiveProfileSerializer(queryset, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
    