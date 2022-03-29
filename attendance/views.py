import datetime
from calendar import Calendar
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import Region
from .models import DailyAttendance

# Create your views here.


@login_required
def get_regions(request):
    regions = Region.objects.filter(is_deleted=False)
    context = {
        "regions": regions,
        "title": "Select Region",
    }
    return render(request, "attendance/regions.html", context)


@login_required
def register_book(request):
    if request.user.is_superuser or request.user.is_global_manager:
        differed_qs = DailyAttendance.objects.distinct("date__year")
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        differed_qs = DailyAttendance.objects.filter(
            user__region=request.user.region
        ).distinct("date__year")
    elif request.user.is_sales_supervisor:
        query_set = DailyAttendance.objects.filter(user__region=request.user.region).distinct("date__year")
        exe_qs = query_set.filter(user__salesexecutive__supervisor__user=request.user)
        mer_qs = query_set.filter(user__merchandiser__executive__supervisor__user=request.user)
        differed_qs = chain(exe_qs,mer_qs)

    years = [i.date.strftime("%Y") for i in differed_qs]
    context = {"is_need_calander": True, "title": "Register Book", "years": years[::-1]}
    return render(request, "attendance/register-book.html", context)


@login_required
def register_page(request):
    date = request.GET.get("date")

    if request.user.is_superuser or request.user.is_global_manager:
        qs = DailyAttendance.objects.filter(date=date)
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        qs = DailyAttendance.objects.filter(date=date, user__region=request.user.region)
    elif request.user.is_sales_supervisor:
        query_set = DailyAttendance.objects.filter(date=date).prefetch_related('user')
        exe_qs = query_set.filter(date=date, user__salesexecutive__supervisor__user=request.user)
        mer_qs = query_set.filter(date=date, user__merchandiser__executive__supervisor__user=request.user)
        qs = chain(exe_qs,mer_qs)

    context = {
        "title": f"Register Book for {date}",
        "attendances": qs,
    }
    return render(request, "attendance/register-page.html", context)


@login_required
def register_page_date(request):
    year = int(request.GET.get("year"))
    month = int(request.GET.get("month"))
    month_name = datetime.date(year, month, 1).strftime("%B")

    c = Calendar()
    dates = [x for x in c.itermonthdates(year, month) if x.month == month]
    context = {
        "title": f"Register Book for {year} - {month_name}",
        "dates": dates,
        "year": year,
        "month": month,
    }
    return render(request, "attendance/register-page-date.html", context)
