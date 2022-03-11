import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from coordinators.forms import (
    SalesCoordinatorForm,
    SalesCoordinatorTargetForm,
    SalesCoordinatorTaskForm,
    SalesManagerForm,
    SalesManagerTargetForm,
    SalesManagerTaskForm,
)
from coordinators.models import (
    SalesCoordinator,
    SalesCoordinatorTarget,
    SalesCoordinatorTask,
    SalesManager,
    SalesManagerTarget,
    SalesManagerTask,
)
from core.functions import generate_form_errors, get_response_data

"""Manager"""


@login_required
def create_manager(request):
    if request.method == "POST":
        form = SalesManagerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:manager_list"),
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
        form = SalesManagerForm()
        context = {
            "form": form,
            "title": "Add Sales Manager",
            "alert_type": "showalert",
        }
        return render(request, "manager/create.html", context)


@login_required
def manager_list(request):
    query_set = SalesManager.objects.filter(is_deleted=False)
    context = {
        "title": "Sales Manger list",
        "instances": query_set,
    }
    return render(request, "manager/list.html", context)


@login_required
def manager_single(request, pk):
    instance = get_object_or_404(SalesManager, pk=pk)
    context = {"title": "Sales manager :- " + instance.name, "instance": instance}
    return render(request, "manager/single.html", context)


@login_required
def update_manager(request, pk):
    instance = get_object_or_404(SalesManager, pk=pk)
    if request.method == "POST":
        form = SalesManagerForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("coordinators:manager_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesManagerForm(instance=instance)
        context = {
            "title": "Edit Sales manager :- " + instance.name,
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/create.html", context)


@login_required
def delete_manager(request, pk):
    SalesManager.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("coordinators:manager_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


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
                1,
                redirect_url=reverse("coordinators:manager_task_list"),
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
        form = SalesManagerTaskForm()
        context = {"form": form, "title": "Add Task", "alert_type": "showalert"}
        return render(request, "manager/task/create.html", context)


@login_required
def manager_task_list(request):
    query_set = SalesManagerTask.objects.filter(is_deleted=False, is_completed=False)
    context = {"title": "Task list", "instances": query_set}
    return render(request, "manager/task/list.html", context)


@login_required
def update_manager_task(request, pk):
    instance = get_object_or_404(SalesManagerTask, pk=pk)
    if request.method == "POST":
        form = SalesManagerTaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:manager_task_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesManagerTaskForm(instance=instance)
        context = {"title": "Edit Task ", "form": form, "instance": instance}
        return render(request, "manager/task/create.html", context)


@login_required
def delete_manager_task(request, pk):
    SalesManagerTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("coordinators:manager_task_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


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
                1,
                redirect_url=reverse("coordinators:manager_target_list"),
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
        form = SalesManagerTargetForm()
        context = {"form": form, "title": "Add Target", "alert_type": "showalert"}
        return render(request, "manager/target/create.html", context)


@login_required
def manager_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    query_set = SalesManagerTarget.objects.filter(
        is_deleted=False, year=year, month=month
    )
    context = {
        "title": "Target list",
        "instances": query_set,
    }
    return render(request, "manager/target/list.html", context)


@login_required
def update_manager_target(request, pk):
    instance = get_object_or_404(SalesManagerTarget, pk=pk)
    if request.method == "POST":
        form = SalesManagerTargetForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:manager_target_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesManagerTargetForm(instance=instance)
        context = {"title": "Edit Target ", "form": form, "instance": instance}
        return render(request, "manager/target/create.html", context)


@login_required
def delete_manager_target(request, pk):
    SalesManagerTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("coordinators:manager_target_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


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
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:coordinator_list"),
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
        form = SalesCoordinatorForm()
        context = {
            "form": form,
            "title": "Add Sales Coordinator",
            "alert_type": "showalert",
        }
        return render(request, "coordinator/create.html", context)


@login_required
def coordinator_list(request):
    if request.user.is_superuser:
        query_set = SalesCoordinator.objects.filter(is_deleted=False)
    else:
        query_set = SalesCoordinator.objects.filter(
            is_deleted=False, region=request.user.region
        )

    context = {
        "title": "Sales Coordinator list",
        "instances": query_set,
    }
    return render(request, "coordinator/list.html", context)


@login_required
def coordinator_single(request, pk):
    instance = get_object_or_404(SalesCoordinator, pk=pk)
    context = {"title": "Sales Coordinator :- " + instance.name, "instance": instance}
    return render(request, "coordinator/single.html", context)


@login_required
def update_coordinator(request, pk):
    instance = get_object_or_404(SalesCoordinator, pk=pk)
    if request.method == "POST":
        form = SalesCoordinatorForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:coordinator_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesCoordinatorForm(instance=instance)
        context = {
            "title": "Edit Sales Coordinator :- " + instance.name,
            "form": form,
            "instance": instance,
        }
        return render(request, "coordinator/create.html", context)


@login_required
def delete_coordinator(request, pk):
    SalesCoordinator.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("coordinators:coordinator_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Coordinator"""

"""Coordinator Task"""


@login_required
def create_coordinator_task(request):
    user = request.user
    if request.method == "POST":
        form = SalesCoordinatorTaskForm(user, request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:coordinator_task_list"),
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
        form = SalesCoordinatorTaskForm(user)
        context = {"form": form, "title": "Add Task", "alert_type": "showalert"}
        return render(request, "coordinator/task/create.html", context)


@login_required
def coordinator_task_list(request):
    if request.user.is_superuser:
        query_set = SalesCoordinatorTask.objects.filter(
            is_deleted=False, is_completed=False
        )
    else:
        query_set = SalesCoordinatorTask.objects.filter(
            is_deleted=False, is_completed=False, user__region=request.user.region
        ).order_by('-created')
    context = {"title": "Task list", "instances": query_set}
    return render(request, "coordinator/task/list.html", context)


@login_required
def update_coordinator_task(request, pk):
    user = request.user
    instance = get_object_or_404(SalesCoordinatorTask, pk=pk)
    if request.method == "POST":
        form = SalesCoordinatorTaskForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:coordinator_task_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesCoordinatorTaskForm(user, instance=instance)
        context = {"title": "Edit Task ", "form": form, "instance": instance}
        return render(request, "coordinator/task/create.html", context)


@login_required
def delete_coordinator_task(request, pk):
    SalesCoordinatorTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("coordinators:coordinator_task_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Coordinator Task"""

"""Coordinator Target"""


@login_required
def create_coordinator_target(request):
    user = request.user
    if request.method == "POST":
        form = SalesCoordinatorTargetForm(user, request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:coordinator_target_list"),
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
        form = SalesCoordinatorTargetForm(user)
        context = {"form": form, "title": "Add Target", "alert_type": "showalert"}
        return render(request, "coordinator/target/create.html", context)


@login_required
def coordinator_target_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year

    if request.user.is_superuser:
        query_set = SalesCoordinatorTarget.objects.filter(
            is_deleted=False, year=year, month=month
        )
    else:
        query_set = SalesCoordinatorTarget.objects.filter(
            is_deleted=False, year=year, month=month, user__region=request.user.region
        )

    context = {
        "title": "Target list",
        "instances": query_set,
    }
    return render(request, "coordinator/target/list.html", context)


@login_required
def update_coordinator_target(request, pk):
    user = request.user
    instance = get_object_or_404(SalesCoordinatorTarget, pk=pk)
    if request.method == "POST":
        form = SalesCoordinatorTargetForm(user, request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("coordinators:coordinator_target_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SalesCoordinatorTargetForm(user, instance=instance)
        context = {"title": "Edit Target ", "form": form, "instance": instance}
        return render(request, "coordinator/target/create.html", context)


@login_required
def delete_coordinator_target(request, pk):
    SalesCoordinatorTarget.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1,
        redirect_url=reverse("coordinators:coordinator_target_list"),
        message="Deleted",
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Coordinator Target"""
