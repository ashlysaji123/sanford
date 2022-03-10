import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data

from .forms import NotificationForm
from .models import Notification

# Create your views here.

"""Notification"""


@login_required
def create_notification(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("notifications:notification_list"),
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
        form = NotificationForm()
        context = {"form": form, "title": "Add notification", "alert_type": "showalert"}
        return render(request, "notification/create.html", context)


@login_required
def notification_list(request):
    query_set = Notification.objects.filter(is_deleted=False)
    context = {
        "title": "Notification list",
        "instances": query_set,
    }
    return render(request, "notification/list.html", context)


@login_required
def update_notification(request, pk):
    instance = get_object_or_404(Notification, pk=pk)
    if request.method == "POST":
        form = NotificationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("notifications:notification_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = NotificationForm(instance=instance)
        context = {"title": "Edit notification ", "form": form, "instance": instance}
        return render(request, "notification/create.html", context)


@login_required
def delete_notification(request, pk):
    Notification.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("notifications:notification_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Notification"""
