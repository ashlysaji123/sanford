import datetime
import json
from datetime import timedelta
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from attendance.models import DailyAttendance
from core.functions import get_response_data
from .models import LeaveRequest

""" 
    global variables
    for multiple functions
"""
today = datetime.datetime.now().date()
current_month = today.month
current_year = today.year


@login_required
def leave_request_list(request):
    if request.user.is_superuser:
        query_set = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            global_manager_approved=True
        )
    if request.user.is_global_manager:
        query_set = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            manager_approved=True
        )
    elif request.user.is_sales_manager:
        query_set = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            user__region=request.user.region
        )
    elif request.user.is_sales_coordinator:
        query_set = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            user__region=request.user.region
        )
    elif request.user.is_sales_supervisor:
        qs = LeaveRequest.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False,
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Pending Leave requests",
        "instances": query_set,
    }
    return render(request, "leave/pending/list.html", context)


@login_required
def approved_leave_list(request):
    if request.method == "GET":
        today = datetime.datetime.now().date()
        if request.user.is_superuser or request.user.is_global_manager:
            query_set = LeaveRequest.objects.filter(
                is_approved=True,
                is_rejected=False,
                is_deleted=False,
                created__date=today
            )
        elif request.user.is_sales_manager or request.user.is_sales_coordinator:
            query_set = LeaveRequest.objects.filter(
                is_deleted=False,
                is_approved=True,
                is_rejected=False,
                user__region=request.user.region,
                created__date=today
            )
        elif request.user.is_sales_supervisor:
            qs = LeaveRequest.objects.filter(
                is_deleted=False,
                is_approved=True,
                is_rejected=False,
                created__date=today
            ).prefetch_related('user')
            exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
            mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
            query_set = chain(exe_qs,mer_qs)
    else:
        date = request.POST.get('date')
        if request.user.is_superuser or request.user.is_global_manager:
            query_set = LeaveRequest.objects.filter(
                is_approved=True,
                is_rejected=False,
                is_deleted=False,
                created__date=date
            )
        elif request.user.is_sales_manager or request.user.is_sales_coordinator:
            query_set = LeaveRequest.objects.filter(
                is_deleted=False,
                is_approved=True,
                is_rejected=False,
                user__region=request.user.region,
                created__date=date
            )
        elif request.user.is_sales_supervisor:
            qs = LeaveRequest.objects.filter(
                is_deleted=False,
                is_approved=True,
                is_rejected=False,
                created__date=date
            ).prefetch_related('user')
            exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
            mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
            query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Approved Leave requests",
        "instances": query_set,
    }
    return render(request, "leave/approved/list.html", context)

def rejected_leave_list(request):
    pass

@login_required
def leave_single(request, pk):
    instance = get_object_or_404(LeaveRequest, pk=pk)
    context = {
        "title": "Leave Request :- " + instance.user.first_name,
        "instance": instance,
    }
    return render(request, "leave/single.html", context)


@login_required
def accept_leave(request, pk):
    leave_data = get_object_or_404(LeaveRequest, pk=pk)
    startdate = leave_data.startdate
    enddate = leave_data.enddate
    if startdate > enddate:
        response_data = get_response_data(0, message="Please check the date!.")
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )

    def mark_attendance(enddate,startdate):
        """ function for updating attandance model """
        delta = enddate - startdate
        for i in range(delta.days + 1):
            day = startdate + timedelta(days=i)
            attandance = DailyAttendance(user=leave_data.user, date=day, is_leave=True)
            attandance.save()
        return None

    if request.user.is_superuser:
        mark_attendance(enddate,startdate)
        leave_data.is_approved = True
        leave_data.is_rejected = False
        leave_data.save()
    if request.user.is_global_manager:
        mark_attendance(enddate,startdate)
        leave_data.is_approved = True
        leave_data.is_rejected = False
        leave_data.global_manager_approved = True
        leave_data.save()
    if request.user.is_sales_manager:
        mark_attendance(enddate,startdate)
        leave_data.is_approved = True
        leave_data.is_rejected = False
        leave_data.manager_approved = True
        leave_data.save()
    elif request.user.is_sales_coordinator:
        mark_attendance(enddate,startdate)
        leave_data.is_approved = True
        leave_data.is_rejected = False
        leave_data.coordinator_approved = True
        leave_data.save()
    elif request.user.is_sales_supervisor:
        leave_data.supervisor_approved = True
        leave_data.supervisor_rejected = False
        leave_data.save()

    response_data = get_response_data(
        1, redirect_url=reverse("leave:approved_leave_list"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def reject_leave(request, pk):
    leave_data = get_object_or_404(LeaveRequest, pk=pk)

    if request.user.is_superuser:
        leave_data.is_approved = False
        leave_data.is_rejected = True
        leave_data.save()
    if  request.user.is_global_manager:
        leave_data.is_approved = False
        leave_data.is_rejected = True
        leave_data.global_manager_rejected = True
        leave_data.save()
    if request.user.is_sales_manager:
        leave_data.is_approved = False
        leave_data.is_rejected = True
        leave_data.manager_rejected = True
        leave_data.save()
    elif request.user.is_sales_coordinator:
        leave_data.is_approved = False
        leave_data.is_rejected = True
        leave_data.coordinator_rejected = True
        leave_data.save()
    elif request.user.is_sales_supervisor:
        leave_data.supervisor_approved = False
        leave_data.supervisor_rejected = True
        leave_data.save()

    response_data = get_response_data(
        1, redirect_url=reverse("leave:leave_request_list"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )
