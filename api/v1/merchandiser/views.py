import datetime

from django.db.models import Avg
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from merchandiser.models import Merchandiser, MerchandiserTarget, MerchandiserTask
from sales.models import Sales,SaleReturn

from .serializers import (
    MerchandiserProfileSerializer,
    MerchandiserTargetSerializer,
    MerchandiserTaskSerializer,
)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def merchandiser_target(request):
    """
    Fetch target based on which user is requesting
    for target and current year and month
    """
    user = request.user
    merchandiser = get_object_or_404(Merchandiser, user=user)
    try:
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        target = MerchandiserTarget.objects.filter(
            user=merchandiser, year=current_year, month=current_month
        )
        serializer = MerchandiserTargetSerializer(
            target, many=True, context={"request": request}
        )
        return Response(serializer.data)
    except MerchandiserTarget.DoesNotExist:
        target = None
        response_data = {
            "status": False,
            "detail": "No Target Assigned",
        }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def merchandiser_task(request):
    """
    Fetch not completed task based on which user is requesting
    for task
    """
    user = request.user
    merchandiser = get_object_or_404(Merchandiser, user=user)
    task = MerchandiserTask.objects.filter(user=merchandiser, is_completed=False)
    serializer = MerchandiserTaskSerializer(
        task, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def merchandiser_completed_task(request):
    """
    Fetch completed task based on which user is requesting
    for task
    """
    user = request.user
    merchandiser = get_object_or_404(Merchandiser, user=user)
    task = MerchandiserTask.objects.filter(user=merchandiser, is_completed=True)
    serializer = MerchandiserTaskSerializer(
        task, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def merchandiser_mark_task(request, pk):
    """
    Marking task as a Completed task
    """
    request.user
    try:
        task = MerchandiserTask.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        response = {
            "status": 200,
            "message": "Successfully Updated.",
        }
        return Response(response, status=status.HTTP_201_CREATED)
    except MerchandiserTask.DoesNotExist:
        raise Http404


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def merchandiser_profile(request):
    try:
        user = request.user
        queryset = Merchandiser.objects.get(user=user)
    except:
        response = "User not found"
        return Response(response, status=status.HTTP_200_OK)

    serializer = MerchandiserProfileSerializer(queryset, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def merchandiser_sale_status(request):
    """
    Fetch merchandaiser sales data
    """
    user = request.user
    merchandiser = get_object_or_404(Merchandiser, user=user)
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    today = datetime.datetime.now().date()
    try:
        target = MerchandiserTarget.objects.get(
            user=merchandiser,
            year=current_year,
            month=current_month,
            target_type="SECONDARY",
        )
        secondry_target = target.target_amount
        current_amount = target.current_amount
        is_target_achieved = False
        if current_amount >= secondry_target:
            is_target_achieved = True
    except MerchandiserTarget.DoesNotExist:
        is_target_achieved = False
        secondry_target = 0
    """Primary target data"""
    if MerchandiserTarget.objects.filter(user=merchandiser, year=current_year, month=current_month,target_type="PRIMARY").exists():
        primary_target_data = MerchandiserTarget.objects.get(user=merchandiser, year=current_year, month=current_month,target_type="PRIMARY")
        primary_target = primary_target_data.target_amount
    else:
        primary_target = 0

    """Primary target data end"""
    """monthly sales data"""
    monthly_sales = Sales.objects.filter(
        user=user,
        created__year=current_year,
        created__month=current_month,
        is_approved=True,
    )
    current_month_sale = 0
    for sale in monthly_sales:
        current_month_sale += sale.total_amount
    """montlys sales avarage"""
    monthly_avarage_sale = Sales.objects.filter(
        user=user,
        created__year=current_year,
        created__month=current_month,
        is_approved=True,
    ).aggregate(Avg("total_amount"))
    """Today sales"""
    today_sale = Sales.objects.filter(user=user, created__date=today)
    today_sale_amount = 0
    for sale in today_sale:
        today_sale_amount += sale.total_amount
    """Monthly sales data end"""
    """Monthly Sales return data """
    total_sales_return = SaleReturn.objects.filter(
        user=user,
        created__month=current_month,
    )
    total_month_sale_return = 0
    for salereturn in total_sales_return:
        total_month_sale_return += salereturn.total_amount
    """Monthly sales return data end"""

    response_data = {
        "status": True,
        "is_target_achieved": is_target_achieved,
        "secondry_target": secondry_target,
        "primary_target": primary_target,
        "current_month_sale": current_month_sale,
        "today_sale_amount": today_sale_amount,
        "monthly_avarage_sale": monthly_avarage_sale,
        "total_month_sale_return":total_month_sale_return
    }
    return Response(response_data)

