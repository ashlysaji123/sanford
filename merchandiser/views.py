from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
import datetime
from core.functions import generate_form_errors, get_response_data
import json
import sys

from .forms import *
from .models import *
from accounts.models import User
from core.functions import get_current_role


"""Manager"""
@login_required
def create_merchandiser(request):
    if request.method == "POST":
        form = MerchandiserForm(request.POST, request.FILES)
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
                    is_merchandiser=True,
                    is_staff=False,
                    photo=photo
                )
                data.user = user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('merchandiser:merchandiser_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = MerchandiserForm()
        context = {
            "form": form,
            "title": "Add Merchandiser",
            "alert_type": "showalert"
        }
        return render(request, 'merchandiser/create.html', context)


@login_required
def merchandiser_list(request):
    query_set = Merchandiser.objects.filter(is_deleted=False)
    context = {
        "is_need_datatable": True,
        "title": "Merchandiser list",
        "instances": query_set
    }
    return render(request, 'merchandiser/list.htm', context)


@login_required
def merchandiser_single(request, pk):
    instance = get_object_or_404(Merchandiser, pk=pk)
    context = {
        "title": "Merchandiser :- " + instance.name,
        "instance": instance
    }
    return render(request, 'merchandiser/single.htm', context)


@login_required
def update_merchandiser(request, pk):
    instance = get_object_or_404(Merchandiser, pk=pk)
    if request.method == 'POST':
        form = MerchandiserForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('merchandiser:merchandiser_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = MerchandiserForm(instance=instance)
        context = {
            "title": "Edit Merchandiser :- " + instance.name,
            "form": form,
            "instance": instance
        }
        return render(request, 'merchandiser/create.html', context)


@login_required
def delete_merchandiser(request, pk):
    Merchandiser.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'merchandiser:merchandiser_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Manager"""



"""Manager Task"""
@login_required
def create_merchandiser_task(request):
    if request.method == "POST":
        form = MerchandiserTaskForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('merchandiser:merchandiser_task_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = MerchandiserTaskForm()
        context = {
            "form": form,
            "title": "Add Task",
            "alert_type": "showalert"
        }
        return render(request, 'merchandiser/task/create.html', context)


@login_required
def merchandiser_task_list(request):
    query_set = MerchandiserTask.objects.filter(is_deleted=False,is_completed=False)
    context = {
        "is_need_datatable": True,
        "title": "Task list",
        "instances": query_set
    }
    return render(request, 'merchandiser/task/list.htm', context)


@login_required
def update_merchandiser_task(request, pk):
    instance = get_object_or_404(MerchandiserTask, pk=pk)
    if request.method == 'POST':
        form = MerchandiserTaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('merchandiser:merchandiser_task_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = MerchandiserTaskForm(instance=instance)
        context = {
            "title": "Edit Task ",
            "form": form,
            "instance": instance
        }
        return render(request, 'merchandiser/task/create.html', context)


@login_required
def delete_merchandiser_task(request, pk):
    MerchandiserTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'merchandiser:merchandiser_task_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Manager Task"""

"""Manager Target"""
@login_required
def create_merchandiser_target(request):
    if request.method == "POST":
        form = MerchandiserTargetForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1, redirect_url=reverse('merchandiser:merchandiser_target_list'), message="Added Successfully.")
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            message = generate_form_errors(form)
            response_data = get_response_data(0, message=message)
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = MerchandiserTargetForm()
        context = {
            "form": form,
            "title": "Add Target",
            "alert_type": "showalert"
        }
        return render(request, 'merchandiser/target/create.html', context)


@login_required
def merchandiser_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    query_set = MerchandiserTarget.objects.filter(is_deleted=False,year=year,month=month)
    context = {
        "is_need_datatable": True,
        "title": "Target list",
        "instances": query_set
    }
    return render(request, 'merchandiser/target/list.htm', context)


@login_required
def update_merchandiser_target(request, pk):
    instance = get_object_or_404(MerchandiserTarget, pk=pk)
    if request.method == 'POST':
        form = MerchandiserTargetForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse('merchandiser:merchandiser_target_list'), message="Updated")
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = MerchandiserTargetForm(instance=instance)
        context = {
            "title": "Edit Target ",
            "form": form,
            "instance": instance
        }
        return render(request, 'merchandiser/target/create.html', context)


@login_required
def delete_merchandiser_target(request, pk):
    MerchandiserTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(1, redirect_url=reverse(
        'merchandiser:merchandiser_target_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')

"""Manager Target"""

