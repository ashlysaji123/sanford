import datetime
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from loans.models import Loan
from salaries.models import SalaryAdavance
from globalstaffs.forms import (
    GlobalManagerForm,
    GlobalManagerTargetForm,
    GlobalManagerTaskForm,
    GlobalManagerUpdateForm
)
from globalstaffs.models import (
    GlobalManager,
    GlobalManagerTarget,
    GlobalManagerTask
)
from core.functions import generate_form_errors, get_response_data

"""Global Manager"""
@login_required
def create_global_manager(request):
    if request.method == "POST":
        form = GlobalManagerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("globalstaffs:global_manager_list"),
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
        form = GlobalManagerForm()
        context = {
            "form": form,
            "title": "Add Global Manager",
            "alert_type": "showalert",
        }
        return render(request, "global-manager/create.html", context)


@login_required
def global_manager_list(request):
    query_set = GlobalManager.objects.filter(is_deleted=False)
    context = {
        "title": "Global Manager list",
        "instances": query_set,
    }
    return render(request, "global-manager/list.html", context)


@login_required
def global_manager_single(request, pk):
    instance = get_object_or_404(GlobalManager, pk=pk)
    context = {
        "title": "Global manager :- " + instance.name, 
        "instance": instance,
    }
    if Loan.objects.filter(is_approved=True,is_returned_completely=False,creator=instance.user).exists():
        loan = Loan.objects.get(is_approved=True,is_returned_completely=False,creator=instance.user)
        context.update({
            "loan" : loan,
        })
    if SalaryAdavance.objects.filter(is_approved=True,is_returned_completely=False,user=instance.user).exists():
        salary_advance = SalaryAdavance.objects.filter(is_approved=True,is_returned_completely=False,user=instance.user)
        context.update({
            "salary_advance" : salary_advance,
        })
    return render(request, "global-manager/single.html", context)


@login_required
def update_global_manager(request, pk):
    instance = get_object_or_404(GlobalManager, pk=pk)
    if request.method == "POST":
        form = GlobalManagerUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("globalstaffs:global_manager_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = GlobalManagerUpdateForm(instance=instance)
        context = {
            "title": "Edit Global manager :- " + instance.name,
            "form": form,
            "instance": instance,
        }
        return render(request, "global-manager/create.html", context)


@login_required
def delete_global_manager(request, pk):
    GlobalManager.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("globalstaffs:global_manager_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Global Manager Task"""
@login_required
def create_global_manager_task(request):
    if request.method == "POST":
        form = GlobalManagerTaskForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("globalstaffs:global_manager_task_list"),
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
        form = GlobalManagerTaskForm()
        context = {"form": form, "title": "Add Task", "alert_type": "showalert"}
        return render(request, "global-manager/task/create.html", context)


@login_required
def global_manager_task_list(request):
    query_set = GlobalManagerTask.objects.filter(is_deleted=False, is_completed=False)
    context = {"title": "Task list", "instances": query_set}
    return render(request, "global-manager/task/list.html", context)


@login_required
def update_global_manager_task(request, pk):
    instance = get_object_or_404(GlobalManagerTask, pk=pk)
    if request.method == "POST":
        form = GlobalManagerTaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("globalstaffs:global_manager_task_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = GlobalManagerTaskForm(instance=instance)
        context = {"title": "Edit Task ", "form": form, "instance": instance}
        return render(request, "global-manager/task/create.html", context)


@login_required
def delete_global_manager_task(request, pk):
    GlobalManagerTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("globalstaffs:global_manager_task_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Global Manager Target"""
@login_required
def create_global_manager_target(request):
    if request.method == "POST":
        form = GlobalManagerTargetForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("globalstaffs:global_manager_target_list"),
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
        form = GlobalManagerTargetForm()
        context = {"form": form, "title": "Add Target", "alert_type": "showalert"}
        return render(request, "global-manager/target/create.html", context)


@login_required
def global_manager_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    query_set = GlobalManagerTarget.objects.filter(
        is_deleted=False, year=year, month=month
    )
    context = {
        "title": "Target list",
        "instances": query_set,
    }
    return render(request, "global-manager/target/list.html", context)


@login_required
def update_global_manager_target(request, pk):
    instance = get_object_or_404(GlobalManagerTarget, pk=pk)
    if request.method == "POST":
        form = GlobalManagerTargetForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("globalstaffs:global_manager_target_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = GlobalManagerTargetForm(instance=instance)
        context = {"title": "Edit Target ", "form": form, "instance": instance}
        return render(request, "global-manager/target/create.html", context)


@login_required
def delete_global_manager_target(request, pk):
    GlobalManagerTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("globalstaffs:global_manager_target_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )

"""Global Manager Target"""

