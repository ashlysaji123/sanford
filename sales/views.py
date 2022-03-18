import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from core.functions import generate_form_errors, get_response_data
from .forms import OpeningStockForm,SelectStaffForm
from .models import OpeningStock, SaleItems, Sales,SaleReturn,SaleReturnItems
from merchandiser.models import MerchandiserTarget,Merchandiser
from executives.models import SalesExecutiveTarget,SalesExecutive
from coordinators.models import SalesCoordinatorTarget,SalesManagerTarget,SalesManager,SalesCoordinator
from accounts.models import User
from sales.utils import reverse_querystring
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

    context = {
        "title": "Sale single page ",
        "instance": instance,
        "sale_items": sale_items,
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
    sale = Sales.objects.get(pk=pk)
    sale.is_rejected=False
    sale.is_approved=True
    user = sale.user

    current_year =  sale.created.year
    current_month =  sale.created.month

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


""" sales return"""
class SaleReturnList(ListView):
    template_name = 'sales/sale/SaleReturn_list.html'
    model = SaleReturn

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sale returns"
        return context

    def get_queryset(self):
        today = datetime.datetime.now().date()
        current_month = today.month
        current_year = today.year
        query = self.kwargs.get('q')
        user = self.request.user
        # query_set = self.model.objects.filter(category=self.kwargs.get('category'))

        if query is None or query == "T":
            if self.request.user.is_superuser:
                query_set = self.model.objects.filter(is_deleted=False,created__date=today)
            else:
                query_set = self.model.objects.filter(is_deleted=False,user__region=user.region,created__date=today)
        elif query == "M":
            if self.request.user.is_superuser:
                query_set = self.model.objects.filter(is_deleted=False,created__date=current_month)
            else:
                query_set = self.model.objects.filter(is_deleted=False,user__region=user.region,created__date=current_month)
        elif query == "Y":
            if self.request.user.is_superuser:
                query_set = self.model.objects.filter(is_deleted=False,created__date=current_year)
            else:
                query_set = self.model.objects.filter(is_deleted=False,user__region=user.region,created__date=current_year)

        return query_set

class SaleReturnDetail(DetailView):
    model = SaleReturn
    template_name = 'sales/sale/SaleReturn_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["return_items"] = SaleReturnItems.objects.filter(sale=self.get_object())
        return context


@login_required
def select_satff_for_reports(request):
    user = request.user
    if request.method == "POST":
        user = request.POST.get('user')
        if user:
            url = reverse_querystring("sales:sales_report", {"user": user})
            return HttpResponseRedirect(url)
    else:
        form = SelectStaffForm(user)
        context = {
            'title': "Select staff",
            "form":form,
        }
        return render(request, "sales/sale/sales-report-staff.html", context)


@login_required
def sales_report(request):
    user_id = request.GET.get("user")
    user = User.objects.get(id=user_id)
    current_year =  datetime.datetime.now().year
    current_month =  datetime.datetime.now().month

    sales_return = SaleReturn.objects.filter(user=user,created__year=current_year,created__month=current_month)
    sales_return_amount = 0
    for i in sales_return:
        sales_return_amount += i.total_amount

    sales_data = Sales.objects.filter(user=user,created__year=current_year,created__month=current_month,is_approved=True)
    sales_amount = 0
    for i in sales_data:
        sales_amount += i.total_amount

    target_data = []
    if Merchandiser.objects.filter(user=user).exists():
        print("merchant")
        merchant = Merchandiser.objects.get(user=user)
        target_data = MerchandiserTarget.objects.filter(year=current_year,month=current_month,user=merchant)
    elif SalesExecutive.objects.filter(user=user).exists():
        print("executives")
        executive = SalesExecutive.objects.get(user=user)
        target_data = SalesExecutiveTarget.objects.filter(year=current_year,month=current_month,user=executive)

    context = {
        "title": "Sale Report ",
        "user": user,
        "target_data":target_data,
        "sales_return_amount":sales_return_amount,
        "sales_amount":sales_amount
    }
    return render(request, "sales/sale/sales-report.html", context)