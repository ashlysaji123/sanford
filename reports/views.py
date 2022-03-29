import json
from queue import Empty
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import datetime
from django.views.generic import DetailView, ListView, TemplateView

from core.functions import generate_form_errors, get_response_data
from .forms import DARNotesForm, DARTaskForm
from .models import CollectMoney, DARNotes, DARTask,DARReschedule,Order, OrderItem,UploadPhoto


"""DAR"""
@login_required
def create_DAR(request):
    user = request.user
    DARFormset = formset_factory(DARNotesForm, extra=1)
    if request.method == "POST":
        form = DARTaskForm(user, request.POST, request.FILES)
        DAR_formset = DARFormset(request.POST, prefix="DAR_formset")
        if form.is_valid() and DAR_formset.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()

            for form in DAR_formset:
                type = form.cleaned_data["type"]
                note = form.cleaned_data["note"]
                DARNotes.objects.create(
                    type=type,
                    note=note,
                    dar=data,
                    creator=request.user,
                )

            response_data = get_response_data(
                1, redirect_url=reverse("reports:DAR_list"), message="DAR Added"
            )
        else:
            message = generate_form_errors(form, formset=False)
            message += generate_form_errors(DAR_formset, formset=True)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = DARTaskForm(user)
        DAR_formset = DARFormset(prefix="DAR_formset")
        context = {
            "title": "Create DAR",
            "form": form,
            "DAR_formset": DAR_formset,
        }
        return render(request, "reports/DAR/create.html", context)


@login_required
def update_DAR(request, pk):
    user = request.user
    instance = get_object_or_404(DARTask, pk=pk)

    if DARNotes.objects.filter(dar=instance).exists():
        extra = 0
    else:
        extra = 1

    DARFormset = inlineformset_factory(
        DARTask,
        DARNotes,
        can_delete=True,
        extra=extra,
        fields=('title','note'),
        widgets={
            "title": TextInput(
                attrs={"class": "required form-control", "placeholder": "Title"}
            ),
            "note": TextInput(
                attrs={"class": "required form-control", "placeholder": "Note"}
            ),
        },
    )
    if request.method == "POST":
        form = DARTaskForm(user, request.POST, request.FILES, instance=instance)
        DAR_formset = DARFormset(request.POST, prefix="DAR_formset", instance=instance)
        print("up of the valicatikjkj")
        if form.is_valid() and DAR_formset.is_valid():
            print("Success reached")
            data = form.save()
            DAR_data = DAR_formset.save(commit=False)
            for item in DAR_data:
                item.dar = data
                item.save()
            for obj in DAR_formset.deleted_objects:
                obj.delete()

            response_data = get_response_data(
                1, redirect_url=reverse("reports:DAR_list"), message="DAR updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            message += generate_form_errors(DAR_formset, formset=True)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = DARTaskForm(user, instance=instance)
        DAR_formset = DARFormset(prefix="DAR_formset", instance=instance)
        context = {
            "title": "Edit DAR",
            "form": form,
            "DAR_formset": DAR_formset,
            "instance": instance,
        }
        return render(request, "reports/DAR/create.html", context)


@login_required
def delete_DAR(request, pk):
    DARTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("reports:DAR_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def DAR_single(request, pk):
    DAR = DARTask.objects.get(pk=pk)
    DAR_data = DARNotes.objects.filter(dar=DAR)
    query_set=[]
    order=[]
    order_item=[]
    photos=[]
    for i in DAR_data:
        if i.type == 'money':
            query_set = CollectMoney.objects.get(dar_note=i)
        elif i.type == 'order':
            order = Order.objects.get(dar_note=i)
            order_item = OrderItem.objects.get(order=query_set)
        elif i.type == 'photo':
            photos = UploadPhoto.objects.get(dar_note=i)

    context = {
        "instance": DAR,
        "DAR_data": DAR_data,
        "query_set":query_set,
        "order":order,
        "order_item":order_item,
        "photos":photos,
        "title": "DAR Single Page",
    }
    return render(request, "reports/DAR/single.html", context)


@login_required
def DAR_list(request):
    if request.method == "GET":
        today = datetime.datetime.now().date()
        query_set = DARTask.objects.filter(
            is_deleted=False, 
            executive__region=request.user.region,
            visit_date=today
        )
        context = {"title": "DAR List", "instances": query_set}
        return render(request, "reports/DAR/list.html", context)
    else:
        date = request.POST.get('date')
        query_set = DARTask.objects.filter(
            is_deleted=False, 
            executive__region=request.user.region,
            visit_date=date
        )
        context = {"title": "DAR List", "instances": query_set}
        return render(request, "reports/DAR/list.html", context)

"""DAR"""

class DARRescheduleList(ListView):
    def get_queryset(self):
        """Returns that belong to the current user"""
        return DARReschedule.objects.filter(
            is_deleted=False,is_approved=False,
            is_rejected=False,
            dar__executive__region=self.request.user.region
        ).prefetch_related('dar')

class DARAcceptedList(ListView):
    template_name = "reports/ddraccepted_list.html"

    def get_queryset(self):
        """Returns that belong to the current user"""
        return DARReschedule.objects.filter(
            is_deleted=False,is_approved=True,
            is_rejected=False,
            dar__executive__region=self.request.user.region
        ).prefetch_related('dar')



@login_required
def accept_reschedule(request,pk):
    data = DARReschedule.objects.get(pk=pk)
    dar = data.dar
    dar.visit_date = data.reschedule_date
    dar.save()
    data.is_approved=True
    data.is_rejected=False
    data.save()
    response_data = get_response_data(
        1, redirect_url=reverse("reports:DAR_reschedule_list"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def reject_reschedule(request, pk):
    DARReschedule.objects.filter(pk=pk).update(is_rejected=True, is_approved=False)
    response_data = get_response_data(
        1, redirect_url=reverse("reports:DAR_reschedule_list"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )



@login_required
def DMRList(request):
    """Returns that belong to the current user region"""
    if request.method == "GET":
        today = datetime.datetime.now().date()
        query_set = DARTask.objects.filter(
            is_deleted=False, 
            executive__region=request.user.region,
            visit_date=today
        )
        context = {"title": "DMR List", "instances": query_set}
    else:
        date = request.POST.get('date')
        query_set = DARTask.objects.filter(
            is_deleted=False, 
            executive__region=request.user.region,
            visit_date=date
        )
        context = {"title": "DMR List", "instances": query_set}
    return render(request, "reports/DMR/list.html", context)



