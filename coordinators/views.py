from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
import datetime
from core.functions import generate_form_errors, get_response_data
import json
import sys

from coordinators.forms import *
from coordinators.models import *
from accounts.models import User
from core.functions import get_current_role
from core.decorators import superuser_only


"""Manager"""
@login_required
def create_manager(request):
    if request.method == "POST":
        form = SalesManagerForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            employe_id = form.cleaned_data["employe_id"]
            photo = form.cleaned_data["photo"]
            if not User.objects.filter(username=phone).exists():
                password = "enduser"
                user = User.objects.create_user(
                    username=phone,
                    first_name=name,
                    password=password,
                    employe_id=employe_id,
                    is_sales_manager=True,
                    is_staff=False,
                    photo=photo
                )
                data.user = user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:manager_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesManagerForm()
        context = {
            "form": form,
            "title": "Add Sales Manager",
            "alert_type": "showalert"
        }
        return render(request, 'manager/create.html', context)


@login_required
def manager_list(request):
    query_set = SalesManager.objects.filter(is_deleted=False)
    context = {
        "is_need_datatable": True,
        "title": "Sales Manger list",
        "instances": query_set
    }
    return render(request, 'manager/list.htm', context)


@login_required
def manager_single(request, pk):
    instance = get_object_or_404(SalesManager, pk=pk)
    context = {
        "title": "Sales manager :- " + instance.name,
        "instance": instance
    }
    return render(request, 'manager/single.htm', context)


@login_required
def update_manager(request, pk):
    instance = get_object_or_404(SalesManager, pk=pk)
    if request.method == 'POST':
        form = SalesManagerForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:manager_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesManagerForm(instance=instance)
        context = {
            "title": "Edit Sales manager :- " + instance.name,
            "form": form,
            "instance": instance
        }
        return render(request, 'manager/create.html', context)


@login_required
def delete_manager(request, pk):
    SalesManager.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'coordinators:manager_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Manager"""



"""Manager Task"""
@login_required
def create_manager_task(request):
    if request.method == "POST":
        form = SalesManagerTaskForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:manager_task_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesManagerTaskForm()
        context = {
            "form": form,
            "title": "Add Task",
            "alert_type": "showalert"
        }
        return render(request, 'manager/task/create.html', context)


@login_required
def manager_task_list(request):
    query_set = SalesManagerTask.objects.filter(is_deleted=False,is_completed=False)
    context = {
        "is_need_datatable": True,
        "title": "Task list",
        "instances": query_set
    }
    return render(request, 'manager/task/list.htm', context)


@login_required
def update_manager_task(request, pk):
    instance = get_object_or_404(SalesManagerTask, pk=pk)
    if request.method == 'POST':
        form = SalesManagerTaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:manager_task_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesManagerTaskForm(instance=instance)
        context = {
            "title": "Edit Task ",
            "form": form,
            "instance": instance
        }
        return render(request, 'manager/task/create.html', context)


@login_required
def delete_manager_task(request, pk):
    SalesManagerTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'coordinators:manager_task_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Manager Task"""

"""Manager Target"""
@login_required
def create_manager_target(request):
    if request.method == "POST":
        form = SalesManagerTargetForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:manager_target_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesManagerTargetForm()
        context = {
            "form": form,
            "title": "Add Target",
            "alert_type": "showalert"
        }
        return render(request, 'manager/target/create.html', context)


@login_required
def manager_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    query_set = SalesManagerTarget.objects.filter(is_deleted=False,year=year,month=month)
    context = {
        "is_need_datatable": True,
        "title": "Target list",
        "instances": query_set
    }
    return render(request, 'manager/target/list.htm', context)


@login_required
def update_manager_target(request, pk):
    instance = get_object_or_404(SalesManagerTarget, pk=pk)
    if request.method == 'POST':
        form = SalesManagerTargetForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:manager_target_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesManagerTargetForm(instance=instance)
        context = {
            "title": "Edit Target ",
            "form": form,
            "instance": instance
        }
        return render(request, 'manager/target/create.html', context)


@login_required
def delete_manager_target(request, pk):
    SalesManagerTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'coordinators:manager_target_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Manager Target"""


"""
Sales Coordinators Creation and task adding  
target creations vies below
"""

"""Coordinator"""
@login_required
def create_coordinator(request):
    if request.method == "POST":
        form = SalesCoordinatorForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            employe_id = form.cleaned_data["employe_id"]
            photo = form.cleaned_data["photo"]
            if not User.objects.filter(username=phone).exists():
                password = "enduser"
                user = User.objects.create_user(
                    username=phone,
                    first_name=name,
                    password=password,
                    employe_id=employe_id,
                    is_sales_coordinator=True,
                    is_staff=False,
                    photo=photo
                )
                data.user = user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:coordinator_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesCoordinatorForm()
        context = {
            "form": form,
            "title": "Add Sales Coordinator",
            "alert_type": "showalert"
        }
        return render(request, 'coordinator/create.html', context)


@login_required
def coordinator_list(request):
    query_set = SalesCoordinator.objects.filter(is_deleted=False)
    context = {
        "is_need_datatable": True,
        "title": "Sales Coordinator list",
        "instances": query_set
    }
    return render(request, 'coordinator/list.htm', context)


@login_required
def coordinator_single(request, pk):
    instance = get_object_or_404(SalesCoordinator, pk=pk)
    context = {
        "title": "Sales Coordinator :- " + instance.name,
        "instance": instance
    }
    return render(request, 'coordinator/single.htm', context)


@login_required
def update_coordinator(request, pk):
    instance = get_object_or_404(SalesCoordinator, pk=pk)
    if request.method == 'POST':
        form = SalesCoordinatorForm(
            request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:coordinator_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesCoordinatorForm(instance=instance)
        context = {
            "title": "Edit Sales Coordinator :- " + instance.name,
            "form": form,
            "instance": instance
        }
        return render(request, 'coordinator/create.html', context)


@login_required
def delete_coordinator(request, pk):
    SalesCoordinator.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'coordinators:coordinator_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Coordinator"""

"""Coordinator Task"""
@login_required
def create_coordinator_task(request):
    if request.method == "POST":
        form = SalesCoordinatorTaskForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:coordinator_task_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesCoordinatorTaskForm()
        context = {
            "form": form,
            "title": "Add Task",
            "alert_type": "showalert"
        }
        return render(request, 'coordinator/task/create.html', context)


@login_required
def coordinator_task_list(request):
    query_set = SalesCoordinatorTask.objects.filter(is_deleted=False,is_completed=False)
    context = {
        "is_need_datatable": True,
        "title": "Task list",
        "instances": query_set
    }
    return render(request, 'coordinator/task/list.htm', context)


@login_required
def update_coordinator_task(request, pk):
    instance = get_object_or_404(SalesCoordinatorTask, pk=pk)
    if request.method == 'POST':
        form = SalesCoordinatorTaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:coordinator_task_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesCoordinatorTaskForm(instance=instance)
        context = {
            "title": "Edit Task ",
            "form": form,
            "instance": instance
        }
        return render(request, 'coordinator/task/create.html', context)


@login_required
def delete_coordinator_task(request, pk):
    SalesCoordinatorTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'coordinators:coordinator_task_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Coordinator Task"""

"""Coordinator Target"""
@login_required
def create_coordinator_target(request):
    if request.method == "POST":
        form = SalesCoordinatorTargetForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:coordinator_target_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesCoordinatorTargetForm()
        context = {
            "form": form,
            "title": "Add Target",
            "alert_type": "showalert"
        }
        return render(request, 'coordinator/target/create.html', context)


@login_required
def coordinator_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    query_set = SalesCoordinatorTarget.objects.filter(is_deleted=False,year=year,month=month)
    context = {
        "is_need_datatable": True,
        "title": "Target list",
        "instances": query_set
    }
    return render(request, 'coordinator/target/list.htm', context)


@login_required
def update_coordinator_target(request, pk):
    instance = get_object_or_404(SalesCoordinatorTarget, pk=pk)
    if request.method == 'POST':
        form = SalesCoordinatorTargetForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('coordinators:coordinator_target_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = SalesCoordinatorTargetForm(instance=instance)
        context = {
            "title": "Edit Target ",
            "form": form,
            "instance": instance
        }
        return render(request, 'coordinator/target/create.html', context)


@login_required
def delete_coordinator_target(request, pk):
    SalesCoordinatorTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'coordinators:coordinator_target_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Coordinator Target"""
