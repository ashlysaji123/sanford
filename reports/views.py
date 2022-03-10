from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
import datetime
import json
import sys
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory

from core.functions import generate_form_errors, get_response_data
from .forms import DARNotesForm,DARTaskForm
from .models import DARTask,DARNotes
from accounts.models import User
from core.functions import get_current_role


"""DAR"""
@login_required
def create_DAR(request):
    user = request.user
    DARFormset = formset_factory(DARNotesForm,extra=1)
    if request.method == 'POST':
        form = DARTaskForm(user,request.POST,request.FILES)
        DAR_formset = DARFormset(request.POST,prefix="DAR_formset")
        if form.is_valid() and DAR_formset.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
    
            for form in DAR_formset:
                title = form.cleaned_data['title']
                note = form.cleaned_data['note']
                DARNotes.objects.create(
                    title = title,
                    note=note,
                    dar=data,
                    creator= request.user,
                )

            response_data = get_response_data(
                1, redirect_url=reverse('reports:DAR_list'), message="DAR Added")
        else:
            message = generate_form_errors(form, formset=False)
            message += generate_form_errors(DAR_formset, formset=True)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = DARTaskForm(user)
        DAR_formset = DARFormset(prefix="DAR_formset")
        context = {
            "title": "Create DAR",
            "form": form,
            "DAR_formset":DAR_formset,
        }
        return render(request, 'reports/DAR/create.htm', context)


@login_required
def update_DAR(request, pk):
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
        exclude=('dar',),
        widgets= {
            'title': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Title'}),
            'note': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Note'}),
        }
    )
    if request.method == 'POST':
        form = DARTaskForm(user,request.POST, request.FILES, instance=instance)
        DAR_formset = DARFormset(
            request.POST, prefix='DAR_formset', instance=instance)
        if form.is_valid() and DAR_formset.is_valid():
            data = form.save()
            DAR_data = DAR_formset.save(commit=False)
            for item in DAR_data:
                item.dar = data
                item.save()
                
            for obj in DAR_formset.deleted_objects:
                obj.delete()

            response_data = get_response_data(
                1, redirect_url=reverse("reports:DAR_list"), message="DAR updated")
        else:
            message = generate_form_errors(form, formset=False)
            message += generate_form_errors(DAR_formset, formset=True)
            response_data = get_response_data(0, message=message)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = DARTaskForm(user,instance=instance)
        DAR_formset = DARFormset(prefix="DAR_formset",instance=instance)
        context = {
            "title": "Edit DAR",
            "form": form,
            "DAR_formset":DAR_formset,
            "instance": instance
        }
        return render(request, 'reports/DAR/create.htm', context)


@login_required
def delete_DAR(request, pk):
    DARTask.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse('reports:DAR_list'), message="Deleted")
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')


@login_required
def DAR_single(request, pk):
    DAR = DARTask.objects.get(pk=pk)
    DAR_data = DARNotes.objects.filter(dar=DAR)
    context = {
        "instance":   DAR,
        "DAR_data":DAR_data,
        "is_need_datatable": True,
        "title": "DAR Single Page"
    }
    return render(request, 'reports/DAR/single.htm', context)


@login_required
def DAR_list(request):
    query_set = DARTask.objects.filter(is_deleted=False,executive__region=request.user.region).order_by('-created')
    context = {
        "is_need_datatable": True,
        "title": "DAR List",
        "instances": query_set
    }
    return render(request, 'reports/DAR/list.htm', context)

"""DAR"""
