from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
import datetime
from core.functions import generate_form_errors,get_response_data
from django.views.decorators.csrf import csrf_exempt
import json
import sys
from calendar import Calendar

from .forms import *
from .models import *
from accounts.models import User
from core.models import Region
# Create your views here.

@login_required
def get_regions(request):
    regions = Region.objects.filter(is_deleted=False)
    context = {
        "regions":regions,
        "title": "Select Region",
    }
    return render(request, 'attendance/regions.html', context)


@login_required
def register_book(request):
    differed_qs = DailyAttendance.objects.distinct('date__year')
    years = [i.date.strftime('%Y') for i in differed_qs]
    context = {
        "is_need_calander": True,
        'title': 'Register Book',
        "years": years[::-1]
    }
    return render(request, 'attendance/register-book.html', context)


@login_required
def register_page(request):
    date = request.GET.get('date')

    qs = DailyAttendance.objects.filter(date=date)

    context = {
        "is_need_datatable": True,
        'title': f'Register Book for {date}',
        "attendances": qs,
    }
    return render(request, 'attendance/register-page.html', context)




@login_required
def register_page_date(request):
    year = int(request.GET.get('year'))
    month = int(request.GET.get('month'))
    month_name = datetime.date(year, month, 1).strftime('%B')

    c = Calendar()
    dates = [x for x in c.itermonthdates(year, month) if x.month == month]
    context = {
        "is_need_datatable": True,
        'title': f'Register Book for {year} - {month_name}',
        "dates": dates,
        "year": year,
        "month": month
    }
    return render(request, 'attendance/register-page-date.html', context)



