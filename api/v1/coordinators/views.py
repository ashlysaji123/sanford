import datetime

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Avg
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from coordinators.models import (
     SalesCoordinator,
     SalesCoordinatorTarget,
     SalesCoordinatorTask,
)

from sales.models import Sales, SaleReturn

from .serializers import ( 
    SalesCoordinatorTargetSerializer,
    SalesCoordinatorTaskSerializer,
    SalesCoordinatorProfileSerializer
)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salescoordinator_target(request):
    """
    Fetch target based on which user is requesting
    for target and current year and month
    """
    user = request.user
    coordinator = get_object_or_404(SalesCoordinator, user=user)
    try:
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        target = SalesCoordinatorTarget.objects.filter(
            user=coordinator, year=current_year, month=current_month
        )
        serializer = SalesCoordinatorTargetSerializer(
            target, many=True, context={"request": request}
        )
        return Response(serializer.data)
    except SalesCoordinatorTarget.DoesNotExist:
        target = None
        response_data = {
            "status": False,
            "detail": "No Target Assigned",
        }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salescoordinator_task(request):
    """
    Fetch not completed task based on which user is requesting
    for task
    """
    user = request.user
    coordinator = get_object_or_404(SalesCoordinator, user=user)
    task = SalesCoordinatorTask.objects.filter(user=coordinator, is_completed=False)
    serializer = SalesCoordinatorTaskSerializer(
        task, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salescoordinator_completed_task(request):
    """
    Fetch completed task based on which user is requesting
    for task
    """
    user = request.user
    coordinator = get_object_or_404(SalesCoordinator, user=user)
    task = SalesCoordinatorTask.objects.filter(user=coordinator, is_completed=True)
    serializer = SalesCoordinatorTaskSerializer(
        task, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def salescoordinator_mark_task(request, pk):
    """
    Marking task as a Completed task
    """
    try:
        task = SalesCoordinatorTask.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        response = {
            "status": 200,
            "message": "Successfully Updated.",
        }
        return Response(response, status=status.HTTP_201_CREATED)
    except SalesCoordinatorTask.DoesNotExist:
        raise Http404


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salescoordinator_profile(request):
    try:
        user = request.user
        queryset = SalesCoordinator.objects.get(user=user)
    except:
        response = "User not found"
        return Response(response, status=status.HTTP_200_OK)
    
    serializer = SalesCoordinatorProfileSerializer(queryset, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def coordinator_sale_status(request):
    """
    Fetch coordinator sales data
    """
    user = request.user
    coordinator = get_object_or_404(SalesCoordinator, user=user)
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    today = datetime.datetime.now().date()
    try:
        target = SalesCoordinatorTarget.objects.get(
            user=coordinator,
            year=current_year,
            month=current_month,
            target_type="SECONDARY",
        )
        primary_target = target.target_amount
        current_amount = target.current_amount
        is_target_achieved = False
        if current_amount >= primary_target:
            is_target_achieved = True
    except SalesCoordinatorTarget.DoesNotExist:
        is_target_achieved = False
        primary_target = 0

        monthly_sales = Sales.objects.filter(
        user=user,
        created__year=current_year,
        created__month=current_month,
        is_approved=True,
    )
    current_month_sale = 0
    for sale in monthly_sales:
        current_month_sale += sale.total_amount
    today_sale = Sales.objects.filter(user=user, created__date=today)
    today_sale_amount = 0
    for sale in today_sale:
        today_sale_amount += sale.total_amount

    monthly_sales_return = SaleReturn.objects.filter(
        user=user,
        created__year=current_year,
        created__month=current_month,
    )
    current_month_sale_return = 0
    for r in monthly_sales_return:
        current_month_sale_return += r.total_amount


    response_data = {
        "status": True,
        "is_target_achieved": is_target_achieved,
        "primary_target": primary_target,
        "current_month_sale": current_month_sale,
        "today_sale_amount": today_sale_amount,
        "current_month_sale_return" : current_month_sale_return
    }
    return Response(response_data)
