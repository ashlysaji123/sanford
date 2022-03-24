import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data

from .forms import (
    SalesExecutiveForm, 
    SalesExecutiveTargetForm, 
    SalesExecutiveTaskForm,
    SalesSupervisorForm, 
    SalesSupervisorTargetForm, 
    SalesSupervisorTaskForm
)
from .models import (
    SalesExecutive, 
    SalesExecutiveTarget, 
    SalesExecutiveTask,
    SalesSupervisor, 
    SalesSupervisorTarget, 
    SalesSupervisorTask
)


"""Executive"""
@login_required
def create_supervisor(request):
    if request.method == "POST":
        form = SalesSupervisorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:supervisor_list"),
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
        form = SalesSupervisorForm()
        context = {
            "form": form,
            "title": "Add Sales Supervisor",
            "alert_type": "showalert",
        }
        return render(request, "supervisor/create.html", context)


@login_required
def supervisor_list(request):
    if request.user.is_superuser:
        query_set = SalesSupervisor.objects.filter(is_deleted=False)
    else:
        query_set = SalesSupervisor.objects.filter(
            is_deleted=False, region=request.user.region
        )

    context = {
        "title": "Sales Supervisor list",
        "instances": query_set,
    }
    return render(request, "supervisor/list.html", context)


@login_required
def supervisor_single(request, pk):
    instance = get_object_or_404(SalesSupervisor, pk=pk)
    context = {"title": "Sales Supervisor :- " + instance.name, "instance": instance}
    return render(request, "supervisor/single.html", context)


@login_required
def update_supervisor(request, pk):
    instance = get_object_or_404(SalesSupervisor, pk=pk)
    if request.method == "POST":
        form = SalesSupervisorForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("executives:supervisor_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesSupervisorForm(instance=instance)
        context = {
            "title": "Edit Sales Supervisor " + instance.name,
            "form": form,
            "instance": instance,
        }
        return render(request, "supervisor/create.html", context)


@login_required
def delete_supervisor(request, pk):
    SalesSupervisor.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("executives:supervisor_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )

"""Supervisor Task"""
@login_required
def create_supervisor_task(request):
    user = request.user
    if request.method == "POST":
        form = SalesSupervisorTaskForm(user, request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:supervisor_task_list"),
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
        form = SalesSupervisorTaskForm(user)
        context = {"form": form, "title": "Add Task", "alert_type": "showalert"}
        return render(request, "supervisor/task/create.html", context)


@login_required
def supervisor_task_list(request):
    if request.user.is_superuser:
        query_set = SalesSupervisorTask.objects.filter(
            is_deleted=False, is_completed=False
        )
    else:
        query_set = SalesSupervisorTask.objects.filter(
            is_deleted=False, is_completed=False, user__region=request.user.region
        )

    context = {"title": "Task list", "instances": query_set}
    return render(request, "supervisor/task/list.html", context)


@login_required
def update_supervisor_task(request, pk):
    user = request.user
    instance = get_object_or_404(SalesSupervisorTask, pk=pk)
    if request.method == "POST":
        form = SalesSupervisorTaskForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:supervisor_task_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesSupervisorTaskForm(user, instance=instance)
        context = {"title": "Edit Task ", "form": form, "instance": instance}
        return render(request, "supervisor/task/create.html", context)


@login_required
def delete_supervisor_task(request, pk):
    SalesSupervisorTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("executives:supervisor_task_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )

"""Supervisor Target"""
@login_required
def create_supervisor_target(request):
    user = request.user
    if request.method == "POST":
        form = SalesSupervisorTargetForm(user, request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:supervisor_target_list"),
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
        form = SalesSupervisorTargetForm(user)
        context = {"form": form, "title": "Add Target", "alert_type": "showalert"}
        return render(request, "supervisor/target/create.html", context)


@login_required
def supervisor_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    if request.user.is_superuser:
        query_set = SalesSupervisorTarget.objects.filter(
            is_deleted=False, year=year, month=month
        )
    else:
        query_set = SalesSupervisorTarget.objects.filter(
            is_deleted=False, year=year, month=month, user__region=request.user.region
        )
    context = {
        "title": "Target list",
        "instances": query_set,
    }
    return render(request, "supervisor/target/list.html", context)


@login_required
def update_supervisor_target(request, pk):
    user = request.user
    instance = get_object_or_404(SalesSupervisorTarget, pk=pk)
    if request.method == "POST":
        form = SalesSupervisorTargetForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:supervisor_target_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesSupervisorTargetForm(user, instance=instance)
        context = {"title": "Edit Target ", "form": form, "instance": instance}
        return render(request, "supervisor/target/create.html", context)


@login_required
def delete_supervisor_target(request, pk):
    SalesSupervisorTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("executives:supervisor_target_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Executive"""
@login_required
def create_executive(request):
    user = request.user
    if request.method == "POST":
        form = SalesExecutiveForm(user,request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:executive_list"),
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
        form = SalesExecutiveForm(user)
        context = {
            "form": form,
            "title": "Add Sales executive",
            "alert_type": "showalert",
        }
        return render(request, "executive/create.html", context)


@login_required
def executive_list(request):
    if request.user.is_superuser:
        query_set = SalesExecutive.objects.filter(is_deleted=False)
    else:
        query_set = SalesExecutive.objects.filter(
            is_deleted=False, region=request.user.region
        )

    context = {
        "title": "Sales executive list",
        "instances": query_set,
    }
    return render(request, "executive/list.html", context)


@login_required
def executive_single(request, pk):
    instance = get_object_or_404(SalesExecutive, pk=pk)
    context = {"title": "Sales Executive :- " + instance.name, "instance": instance}
    return render(request, "executive/single.html", context)


@login_required
def update_executive(request, pk):
    user = request.user
    instance = get_object_or_404(SalesExecutive, pk=pk)
    if request.method == "POST":
        form = SalesExecutiveForm(user,request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("executives:executive_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesExecutiveForm(user,instance=instance)
        context = {
            "title": "Edit Sales executive " + instance.name,
            "form": form,
            "instance": instance,
        }
        return render(request, "executive/create.html", context)


@login_required
def delete_executive(request, pk):
    SalesExecutive.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("executives:executive_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )

"""Executive Task"""
@login_required
def create_executive_task(request):
    user = request.user
    if request.method == "POST":
        form = SalesExecutiveTaskForm(user, request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:executive_task_list"),
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
        form = SalesExecutiveTaskForm(user)
        context = {"form": form, "title": "Add Task", "alert_type": "showalert"}
        return render(request, "executive/task/create.html", context)


@login_required
def executive_task_list(request):
    if request.user.is_superuser:
        query_set = SalesExecutiveTask.objects.filter(
            is_deleted=False, is_completed=False
        )
    else:
        query_set = SalesExecutiveTask.objects.filter(
            is_deleted=False, is_completed=False, user__region=request.user.region
        )

    context = {"title": "Task list", "instances": query_set}
    return render(request, "executive/task/list.html", context)


@login_required
def update_executive_task(request, pk):
    user = request.user
    instance = get_object_or_404(SalesExecutiveTask, pk=pk)
    if request.method == "POST":
        form = SalesExecutiveTaskForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:executive_task_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesExecutiveTaskForm(user, instance=instance)
        context = {"title": "Edit Task ", "form": form, "instance": instance}
        return render(request, "executive/task/create.html", context)


@login_required
def delete_executive_task(request, pk):
    SalesExecutiveTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("executives:executive_task_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )

"""Executive Target"""
@login_required
def create_executive_target(request):
    user = request.user
    if request.method == "POST":
        form = SalesExecutiveTargetForm(user, request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:executive_target_list"),
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
        form = SalesExecutiveTargetForm(user)
        context = {"form": form, "title": "Add Target", "alert_type": "showalert"}
        return render(request, "executive/target/create.html", context)


@login_required
def executive_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    if request.user.is_superuser:
        query_set = SalesExecutiveTarget.objects.filter(
            is_deleted=False, year=year, month=month
        )
    else:
        query_set = SalesExecutiveTarget.objects.filter(
            is_deleted=False, year=year, month=month, user__region=request.user.region
        )
    context = {
        "title": "Target list",
        "instances": query_set,
    }
    return render(request, "executive/target/list.html", context)


@login_required
def update_executive_target(request, pk):
    user = request.user
    instance = get_object_or_404(SalesExecutiveTarget, pk=pk)
    if request.method == "POST":
        form = SalesExecutiveTargetForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("executives:executive_target_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesExecutiveTargetForm(user, instance=instance)
        context = {"title": "Edit Target ", "form": form, "instance": instance}
        return render(request, "executive/target/create.html", context)


@login_required
def delete_executive_target(request, pk):
    SalesExecutiveTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("executives:executive_target_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )

