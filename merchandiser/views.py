import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data

from .forms import MerchandiserForm, MerchandiserTargetForm, MerchandiserTaskForm
from .models import Merchandiser, MerchandiserTarget, MerchandiserTask

"""Manager"""


@login_required
def create_merchandiser(request):
    user = request.user
    if request.method == "POST":
        form = MerchandiserForm(user,request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("merchandiser:merchandiser_list"),
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
        form = MerchandiserForm(user)
        context = {"form": form, "title": "Add Merchandiser", "alert_type": "showalert"}
        return render(request, "merchandiser/create.html", context)


@login_required
def merchandiser_list(request):
    if request.user.is_superuser:
        query_set = Merchandiser.objects.filter(is_deleted=False)
    else:
        query_set = Merchandiser.objects.filter(
            is_deleted=False, state__country__region=request.user.region
        )
    context = {
        "title": "Merchandiser list",
        "instances": query_set,
    }
    return render(request, "merchandiser/list.html", context)


@login_required
def merchandiser_single(request, pk):
    instance = get_object_or_404(Merchandiser, pk=pk)
    context = {"title": "Merchandiser :- " + instance.name, "instance": instance}
    return render(request, "merchandiser/single.html", context)


@login_required
def update_merchandiser(request, pk):
    user = request.user
    instance = get_object_or_404(Merchandiser, pk=pk)
    if request.method == "POST":
        form = MerchandiserForm(user,request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("merchandiser:merchandiser_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = MerchandiserForm(user,instance=instance)
        context = {
            "title": "Edit Merchandiser :- " + instance.name,
            "form": form,
            "instance": instance,
        }
        return render(request, "merchandiser/create.html", context)


@login_required
def delete_merchandiser(request, pk):
    Merchandiser.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("merchandiser:merchandiser_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Manager"""


"""Manager Task"""


@login_required
def create_merchandiser_task(request):
    if request.method == "POST":
        form = MerchandiserTaskForm(request.user, request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("merchandiser:merchandiser_task_list"),
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
        form = MerchandiserTaskForm(request.user)
        context = {"form": form, "title": "Add Task", "alert_type": "showalert"}
        return render(request, "merchandiser/task/create.html", context)


@login_required
def merchandiser_task_list(request):
    if request.user.is_superuser:
        query_set = MerchandiserTask.objects.filter(
            is_deleted=False, is_completed=False
        )
    else:
        query_set = MerchandiserTask.objects.filter(
            is_deleted=False,
            is_completed=False,
            user__state__country__region=request.user.region,
        )
    context = {"title": "Task list", "instances": query_set}
    return render(request, "merchandiser/task/list.html", context)


@login_required
def update_merchandiser_task(request, pk):
    user = request.user
    instance = get_object_or_404(MerchandiserTask, pk=pk)
    if request.method == "POST":
        form = MerchandiserTaskForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("merchandiser:merchandiser_task_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = MerchandiserTaskForm(user, instance=instance)
        context = {"title": "Edit Task ", "form": form, "instance": instance}
        return render(request, "merchandiser/task/create.html", context)


@login_required
def delete_merchandiser_task(request, pk):
    MerchandiserTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1,
        redirect_url=reverse("merchandiser:merchandiser_task_list"),
        message="Deleted",
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Manager Task"""

"""Manager Target"""


@login_required
def create_merchandiser_target(request):
    user = request.user
    if request.method == "POST":
        form = MerchandiserTargetForm(user, request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("merchandiser:merchandiser_target_list"),
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
        form = MerchandiserTargetForm(user)
        context = {"form": form, "title": "Add Target", "alert_type": "showalert"}
        return render(request, "merchandiser/target/create.html", context)


@login_required
def merchandiser_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    if request.user.is_superuser:
        query_set = MerchandiserTarget.objects.filter(
            is_deleted=False, year=year, month=month
        )
    else:
        query_set = MerchandiserTarget.objects.filter(
            is_deleted=False,
            year=year,
            month=month,
            user__state__country__region=request.user.region,
        )
    context = {
        "title": "Target list",
        "instances": query_set,
    }
    return render(request, "merchandiser/target/list.html", context)


@login_required
def update_merchandiser_target(request, pk):
    user = request.user
    instance = get_object_or_404(MerchandiserTarget, pk=pk)
    if request.method == "POST":
        form = MerchandiserTargetForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("merchandiser:merchandiser_target_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = MerchandiserTargetForm(user, instance=instance)
        context = {"title": "Edit Target ", "form": form, "instance": instance}
        return render(request, "merchandiser/target/create.html", context)


@login_required
def delete_merchandiser_target(request, pk):
    MerchandiserTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1,
        redirect_url=reverse("merchandiser:merchandiser_target_list"),
        message="Deleted",
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Manager Target"""
