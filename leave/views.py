from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
import datetime
import json
import sys
from datetime import date, timedelta

from core.functions import generate_form_errors, get_response_data
from .models import *
from attendance.models import DailyAttendance


""" 
    global variables
    for multiple functions
""" 
today = datetime.datetime.now().date()
current_month = today.month
current_year = today.year


@login_required
def leave_request_list(request):
    query = request.GET.get('q')

    if query is None or query == "T":
        if request.user.is_superuser:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=False,is_rejected=False,created__date=today)
        else:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=False,is_rejected=False,created__date=today,user__region=request.user.region)
    elif query == "M":
        if request.user.is_superuser:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=False,is_rejected=False,created__month=current_month)
        else:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=False,is_rejected=False,created__month=current_month,user__region=request.user.region)
    elif query == "Y":
        if request.user.is_superuser:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=False,is_rejected=False,created__year=current_year)
        else:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=False,is_rejected=False,created__year=current_year,user__region=request.user.region)

    context = {
        "is_need_datatable": True,
        "title": "Leave requests",
        "instances": query_set
    }
    return render(request, 'leave/pending/list.htm', context)


@login_required
def approved_leave_list(request):
    query = request.GET.get('q')

    if query is None or query == "T":
        if request.user.is_superuser:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=True,is_rejected=False,created__date=today)
        else:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=True,is_rejected=False,created__date=today,user__region=request.user.region)
    elif query == "M":
        if request.user.is_superuser:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=True,is_rejected=False,created__month=current_month)
        else:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=True,is_rejected=False,created__month=current_month,user__region=request.user.region)
    elif query == "Y":
        if request.user.is_superuser:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=True,is_rejected=False,created__year=current_year)
        else:
            query_set = LeaveRequest.objects.filter(is_deleted=False,is_approved=True,is_rejected=False,created__year=current_year,user__region=request.user.region)

    context = {
        "is_need_datatable": True,
        "title": "Approved Leave requests",
        "instances": query_set
    }
    return render(request, 'leave/approved/list.htm', context)



@login_required
def leave_single(request, pk):
    instance = get_object_or_404(LeaveRequest, pk=pk)
    context = {
        "title": "Leave Request :- " + instance.user.first_name,
        "instance": instance
    }
    return render(request, 'leave/single.htm', context)



@login_required
def accept_leave(request, pk):
    leave_data = get_object_or_404(LeaveRequest,pk=pk)
    startdate = leave_data.startdate
    enddate = leave_data.enddate
    if startdate > enddate:
        response_data = get_response_data(0, message="Please check the date!.")
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    """ function for updating attandance model """
    delta = enddate - startdate  
    for i in range(delta.days + 1):
        day = startdate + timedelta(days=i)
        attandance = DailyAttendance(
                user=leave_data.user,
                date=day,
                is_leave=True
            )
        attandance.save()

    leave_data.is_approved = True
    leave_data.is_rejected = False
    leave_data.save()
    response_data = get_response_data(1, redirect_url=reverse(
        'leave:approved_leave_list'), message="Approved")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')



@login_required
def reject_leave(request, pk):
    LeaveRequest.objects.filter(pk=pk).update(is_rejected=True,is_approved=False)
    response_data = get_response_data(1, redirect_url=reverse(
        'leave:leave_request_list'), message="Rejected")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')