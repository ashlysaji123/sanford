import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data

from .forms import OpeningStockForm
from .models import OpeningStock, SaleItems, Sales

from merchandiser.models import MerchandiserTarget
from executives.models import SalesExecutiveTarget
from coordinators.models import SalesCoordinatorTarget,SalesManagerTarget
# Create your views here.


"""Opening stock """


@login_required
def create_opening_stock(request):
    user = request.user
    if request.method == "POST":
        form = OpeningStockForm(user, request.POST)
        if form.is_valid():
            product = form.cleaned_data["product"]
            qty = form.cleaned_data["count"]
            if OpeningStock.objects.filter(product=product, is_deleted=False).exists():
                instance = OpeningStock.objects.get(product=product, is_deleted=False)
                instance.count += qty
                instance.save()
                response_data = get_response_data(
                    1,
                    redirect_url=reverse("sales:opening_stock_list"),
                    message="Stock updated Successfully.",
                )
            else:
                data = form.save(commit=False)
                data.creator = request.user
                form.save()
                response_data = get_response_data(
                    1,
                    redirect_url=reverse("sales:opening_stock_list"),
                    message="Added Successfully.",
                )
            return HttpResponse(
                json.dumps(response_data), content_type="application/javascript"
            )
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(
                json.dumps(response_data), content_type="application/javascript"
            )
    else:
        form = OpeningStockForm(user)
        context = {
            "form": form,
            "title": "Add Opening stock",
            "alert_type": "showalert",
        }
        return render(request, "sales/stock/create.html", context)


@login_required
def opening_stock_list(request):
    query_set = OpeningStock.objects.filter(is_deleted=False)
    context = {
        "title": "Opening stock list",
        "instances": query_set,
    }
    return render(request, "sales/stock/list.html", context)


@login_required
def update_opening_stock(request, pk):
    user = request.user
    instance = get_object_or_404(OpeningStock, pk=pk)
    if request.method == "POST":
        form = OpeningStockForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("sales:opening_stock_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = OpeningStockForm(user, instance=instance)
        context = {"title": "Edit Opening stock", "form": form, "instance": instance}
        return render(request, "sales/stock/create.html", context)


@login_required
def delete_opening_stock(request, pk):
    OpeningStock.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("sales:opening_stock_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Opening stock"""

""" sales data """


@login_required
def total_sales(request):
    today = datetime.datetime.now().date()
    current_month = today.month
    current_year = today.year
    query = request.GET.get("q")

    if query is None or query == "T":
        if request.user.is_superuser:
            query_set = Sales.objects.filter(
                is_deleted=False, is_approved=True, created__date=today
            )
        else:
            query_set = Sales.objects.filter(
                is_deleted=False,
                is_approved=True,
                created__date=today,
                user__region=request.user.region,
            )
    elif query == "M":
        if request.user.is_superuser:
            query_set = Sales.objects.filter(
                is_deleted=False, is_approved=True, created__month=current_month
            )
        else:
            query_set = Sales.objects.filter(
                is_deleted=False,
                is_approved=True,
                created__month=current_month,
                user__region=request.user.region,
            )
    elif query == "Y":
        if request.user.is_superuser:
            query_set = Sales.objects.filter(
                is_deleted=False, is_approved=True, created__year=current_year
            )
        else:
            query_set = Sales.objects.filter(
                is_deleted=False,
                is_approved=True,
                created__year=current_year,
                user__region=request.user.region,
            )

    context = {
        "title": "Sales Data ",
        "instances": query_set,
    }
    return render(request, "sales/sale/list.html", context)


@login_required
def sales_single(request, pk):
    instance = get_object_or_404(Sales, pk=pk)
    sale_items = SaleItems.objects.filter(sale=instance).distinct("product")
    user = instance.user
    target_data = []

    current_year =  datetime.date.today().year
    current_month =  datetime.date.today().month

    if user.is_merchandiser:
        target_data = MerchandiserTarget.objects.filter(year=current_year,month=current_month)
    elif user.is_sales_executive:
        target_data = SalesExecutiveTarget.objectsfilter(year=current_year,month=current_month)
    elif user.is_sales_coordinator:
        target_data = SalesCoordinatorTarget.objectsfilter(year=current_year,month=current_month)
    elif user.is_sales_manager:
        target_data = SalesManagerTarget.objectsfilter(year=current_year,month=current_month)

    context = {
        "title": "Sale single page ",
        "instance": instance,
        "sale_items": sale_items,
        "target_data":target_data,
    }
    return render(request, "sales/sale/single.html", context)


""" sales data """


@login_required
def pending_sales_requests(request):
    if request.user.is_superuser:
        query_set = Sales.objects.filter(
            is_deleted=False, is_approved=False, is_rejected=False
        )
    else:
        query_set = Sales.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            user__region=request.user.region,
        )

    context = {
        "title": "Pending Sales",
        "instances": query_set,
    }
    return render(request, "sales/pending/list.html", context)


@login_required
def sales_single_pending(request, pk):
    instance = get_object_or_404(Sales, pk=pk)
    sale_items = SaleItems.objects.filter(sale=instance).distinct("product")
    context = {
        "title": "Sale single page ",
        "instance": instance,
        "sale_items": sale_items,
    }
    return render(request, "sales/pending/single.html", context)


@login_required
def accept_sales(request, pk):
    current_year =  datetime.date.today().year
    current_month =  datetime.date.today().month

    sale = Sales.objects.get(pk=pk)
    sale.is_rejected=False
    sale.is_approved=True
    user = sale.user

    if user.is_merchandiser:
        target_data = MerchandiserTarget.objects.get(year=current_year,month=current_month,target_type="SECONDARY")
        target_data.current_amount += sale.total_amount
        if target_data.current_amount >= target_data.target_amount:
            target_data.is_completed=True
        target_data.save()
    elif user.is_sales_executive:
        target_data = SalesExecutiveTarget.objects.get(year=current_year,month=current_month,target_type="SECONDARY")
        target_data.current_amount += sale.total_amount
        if target_data.current_amount >= target_data.target_amount:
            target_data.is_completed=True
        target_data.save()
    elif user.is_sales_coordinator:
        target_data = SalesCoordinatorTarget.objects.get(year=current_year,month=current_month,target_type="SECONDARY")
        target_data.current_amount += sale.total_amount
        if target_data.current_amount >= target_data.target_amount:
            target_data.is_completed=True
        target_data.save()
    elif user.is_sales_manager:
        target_data = SalesManagerTarget.objects.get(year=current_year,month=current_month,target_type="SECONDARY")
        target_data.current_amount += sale.total_amount
        if target_data.current_amount >= target_data.target_amount:
            target_data.is_completed=True
        target_data.save()

    sale.save()

    response_data = get_response_data(
        1, redirect_url=reverse("sales:pending_sales_requests"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def reject_sales(request, pk):
    Sales.objects.filter(pk=pk).update(is_rejected=True, is_approved=False)
    response_data = get_response_data(
        1, redirect_url=reverse("sales:pending_sales_requests"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )
