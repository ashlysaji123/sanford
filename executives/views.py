from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
import datetime
from core.functions import generate_form_errors,get_response_data
import json
import sys

from .forms import *
from .models import *
from accounts.models import User
from core.functions import get_current_role


"""Executive"""
@login_required
def create_executive(request):
    if request.method == "POST":
        form = SalesExecutiveForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('executives:executive_list') ,message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesExecutiveForm()
        context = {
            "form": form,
            "title": "Add Sales executive",
            "alert_type": "showalert"
        }
        return render(request, 'executive/create.html', context)


@login_required
def executive_list(request):
    if request.user.is_superuser:
        query_set = SalesExecutive.objects.filter(is_deleted=False)
    else:
        query_set = SalesExecutive.objects.filter(is_deleted=False,region=request.user.region)

    context = {
        "is_need_datatable": True,
        "title": "Sales executive list",
        "instances": query_set
    }
    return render(request, 'executive/list.htm', context)



@login_required
def executive_single(request, pk):
    instance = get_object_or_404(SalesExecutive, pk=pk)
    context = {
        "title": "Sales Executive :- " + instance.name,
        "instance": instance
    }
    return render(request, 'executive/single.htm', context)



@login_required
def update_executive(request,pk):
    instance = get_object_or_404(SalesExecutive, pk=pk)
    if request.method == 'POST':
        form = SalesExecutiveForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('executives:executive_list') ,message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesExecutiveForm(instance=instance)
        context = {
            "title": "Edit Sales executive " + instance.name,
            "form": form,
            "instance": instance
        }
        return render(request, 'executive/create.html', context)

@login_required
def delete_executive(request,pk):
    SalesExecutive.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'executive:executive_list'),message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Executive"""


"""Executive Task"""
@login_required
def create_executive_task(request):
    user = request.user
    if request.method == "POST":
        form = SalesExecutiveTaskForm(user,request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('executives:executive_task_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesExecutiveTaskForm(user)
        context = {
            "form": form,
            "title": "Add Task",
            "alert_type": "showalert"
        }
        return render(request, 'executive/task/create.html', context)


@login_required
def executive_task_list(request):
    if request.user.is_superuser:
        query_set = SalesExecutiveTask.objects.filter(is_deleted=False,is_completed=False)
    else:
        query_set = SalesExecutiveTask.objects.filter(is_deleted=False,is_completed=False,user__region=request.user.region)

    context = {
        "is_need_datatable": True,
        "title": "Task list",
        "instances": query_set
    }
    return render(request, 'executive/task/list.htm', context)


@login_required
def update_executive_task(request, pk):
    user = request.user
    instance = get_object_or_404(SalesExecutiveTask, pk=pk)
    if request.method == 'POST':
        form = SalesExecutiveTaskForm(user,request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('executives:executive_task_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesExecutiveTaskForm(user,instance=instance)
        context = {
            "title": "Edit Task ",
            "form": form,
            "instance": instance
        }
        return render(request, 'executive/task/create.html', context)


@login_required
def delete_executive_task(request, pk):
    SalesExecutiveTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'executives:executive_task_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Executive Task"""

"""Executive Target"""
@login_required
def create_executive_target(request):
    user = request.user
    if request.method == "POST":
        form = SalesExecutiveTargetForm(user,request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('executives:executive_target_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesExecutiveTargetForm(user)
        context = {
            "form": form,
            "title": "Add Target",
            "alert_type": "showalert"
        }
        return render(request, 'executive/target/create.html', context)


@login_required
def executive_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    if request.user.is_superuser:
        query_set = SalesExecutiveTarget.objects.filter(is_deleted=False,year=year,month=month)
    else:
        query_set = SalesExecutiveTarget.objects.filter(is_deleted=False,year=year,month=month,user__region=request.user.region)
    context = {
        "is_need_datatable": True,
        "title": "Target list",
        "instances": query_set
    }
    return render(request, 'executive/target/list.htm', context)


@login_required
def update_executive_target(request, pk):
    user= request.user
    instance = get_object_or_404(SalesExecutiveTarget, pk=pk)
    if request.method == 'POST':
        form = SalesExecutiveTargetForm(user,request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('executives:executive_target_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesExecutiveTargetForm(user,instance=instance)
        context = {
            "title": "Edit Target ",
            "form": form,
            "instance": instance
        }
        return render(request, 'executive/target/create.html', context)


@login_required
def delete_executive_target(request, pk):
    SalesExecutiveTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'executives:executive_target_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Executive Target"""
