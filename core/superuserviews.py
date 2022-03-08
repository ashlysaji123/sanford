from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
import datetime
import json
import sys

from core.functions import get_response_data
from sales.models import Sales,SaleItems


@login_required
def last_month_sales(request):
    now = datetime.datetime.now()
    first_month = now.month
    second_month = now.month-1 if now.month > 1 else 12
    third_month = now.month-2 if now.month > 2 else 12
    forth_month = now.month-3 if now.month > 3 else 12
    five_month = now.month-4 if now.month > 4 else 12
    sixth_month = now.month-5 if now.month > 5 else 12

    month_names = [now.strftime("%B")[:3]]
    for _ in range(0, 6-1):
        now = now.replace(day=1) - datetime.timedelta(days=1)
        month_names.append(now.strftime("%B")[:3])

    labels = month_names
    sales_list = []

    if request.user.is_superuser:
        first_month_sales = Sales.objects.filter(is_approved=True,created__month=first_month)
    else:
        first_month_sales = Sales.objects.filter(
            is_approved=True,
            created__month=first_month,
            user__region=request.user.region
        )

    first_month_sale_amount = 0
    for i in first_month_sales:
        first_month_sale_amount += i.total_amount
    sales_list.append(first_month_sale_amount)

    if request.user.is_superuser:
        second_month_sales = Sales.objects.filter(is_approved=True,created__month=second_month)
    else:
        second_month_sales = Sales.objects.filter(
            is_approved=True,
            created__month=second_month,
            user__region=request.user.region
        )

    second_month_sale_amount = 0
    for i in second_month_sales:
        second_month_sale_amount += i.total_amount
    sales_list.append(second_month_sale_amount)


    if request.user.is_superuser:
        third_month_sales = Sales.objects.filter(is_approved=True,created__month=third_month)
    else:
        third_month_sales = Sales.objects.filter(
            is_approved=True,
            created__month=third_month,
            user__region=request.user.region
        )

    third_month_sale_amount = 0
    for i in third_month_sales:
        third_month_sale_amount += i.total_amount
    sales_list.append(third_month_sale_amount)


    if request.user.is_superuser:
        forth_month_sales = Sales.objects.filter(is_approved=True,created__month=forth_month)
    else:
        forth_month_sales = Sales.objects.filter(
            is_approved=True,
            created__month=forth_month,
            user__region=request.user.region
        )

    forth_month_sale_amount = 0
    for i in forth_month_sales:
        forth_month_sale_amount += i.total_amount
    sales_list.append(forth_month_sale_amount)


    if request.user.is_superuser:
        five_month_sales = Sales.objects.filter(is_approved=True,created__month=five_month)
    else:
        five_month_sales = Sales.objects.filter(
            is_approved=True,
            created__month=five_month,
            user__region=request.user.region
        )

    five_month_sale_amount = 0
    for i in five_month_sales:
        five_month_sale_amount += i.total_amount
    sales_list.append(five_month_sale_amount)


    if request.user.is_superuser:
        sixth_month_sales = Sales.objects.filter(is_approved=True,created__month=sixth_month)
    else:
        sixth_month_sales = Sales.objects.filter(
            is_approved=True,
            created__month=sixth_month,
            user__region=request.user.region
        )

    sixth_month_sale_amount = 0
    for i in sixth_month_sales:
        sixth_month_sale_amount += i.total_amount
    sales_list.append(sixth_month_sale_amount)

    return JsonResponse(data={
        'labels': labels,
        'revenue_list': sales_list,
    })

