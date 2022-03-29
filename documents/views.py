import imp
from django.shortcuts import render
import datetime
import json
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from itertools import chain

from core.functions import generate_form_errors, get_response_data
from .models import EmployeeDocumentsItems,EmployeeDocuments
# Create your views here.


@login_required
def pending_documents(request):
    if request.user.is_superuser:
        query_set = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            global_manager_approved=True
        )
    if request.user.is_global_manager:
        query_set = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            manager_approved=True
        )
    elif request.user.is_sales_manager:
        query_set = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            user__region=request.user.region
        )
    elif request.user.is_sales_coordinator:
        query_set = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            user__region=request.user.region
        )
    elif request.user.is_sales_supervisor:
        qs = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False,
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Pending Documents",
        "instances": query_set,
    }
    return render(request, "docs/pending_documents.html", context)

@login_required
def documents_single(request, pk):
    instance = get_object_or_404(EmployeeDocuments, pk=pk)
    document_items = EmployeeDocumentsItems.objects.filter(document=instance)
    context = {
        "title": "Document single page ",
        "instance": instance,
        "document_items": document_items,
    }
    return render(request, "docs/single.html", context)



@login_required
def accept_documents(request, pk):
    document = get_object_or_404(EmployeeDocuments,pk=pk)
    if request.user.is_superuser:
        document.is_approved = True
        document.is_rejected = False
        document.save()
    if request.user.is_global_manager:
        document.is_approved = True
        document.is_rejected = False
        document.global_manager_approved = True
        document.save()
    if request.user.is_sales_manager:
        document.is_approved = True
        document.is_rejected = False
        document.manager_approved = True
        document.save()
    elif request.user.is_sales_coordinator:
        document.is_approved = True
        document.is_rejected = False
        document.coordinator_approved = True
        document.save()
    elif request.user.is_sales_supervisor:
        document.supervisor_approved = True
        document.supervisor_rejected = False
        document.save()

    response_data = get_response_data(
        1, redirect_url=reverse("documents:pending_documents"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )



@login_required
def reject_documents(request, pk):
    document = get_object_or_404(EmployeeDocuments,pk=pk)
    if request.user.is_superuser:
        document.is_approved = False
        document.is_rejected = True
        document.save()
    if request.user.is_global_manager:
        document.is_approved = False
        document.is_rejected = True
        document.global_manager_rejected = True
        document.save()
    if request.user.is_sales_manager:
        document.is_approved = False
        document.is_rejected = True
        document.manager_rejected = True
        document.save()
    elif request.user.is_sales_coordinator:
        document.is_approved = False
        document.is_rejected = True
        document.coordinator_rejected = True
        document.save()
    elif request.user.is_sales_supervisor:
        document.supervisor_approved = False
        document.supervisor_rejected = True
        document.save()
        
    response_data = get_response_data(
        1, redirect_url=reverse("documents:pending_documents"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def accepted_documents(request):
    if request.user.is_superuser or request.user.is_global_manager:
        query_set = EmployeeDocuments.objects.filter(
            is_approved=True,
            is_rejected=False,
            is_deleted=False
        )
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        query_set = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
            user__region=request.user.region,
        )
    elif request.user.is_sales_supervisor:
        qs = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Accepted List",
        "instances": query_set,
    }
    return render(request, "docs/pending_documents.html", context)


@login_required
def rejected_documents(request):
    if request.user.is_superuser or request.user.is_global_manager:
        query_set = EmployeeDocuments.objects.filter(
            is_approved=False,
            is_rejected=True,
            is_deleted=False
        )
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        query_set = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=True,
            user__region=request.user.region,
        )
    elif request.user.is_sales_supervisor:
        qs = EmployeeDocuments.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=True,
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Rejected list",
        "instances": query_set,
    }
    return render(request, "docs/pending_documents.html", context)

