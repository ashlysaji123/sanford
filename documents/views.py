import imp
from django.shortcuts import render
import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data

from .models import EmployeeDocumentsItems,EmployeeDocuments
# Create your views here.

@login_required
def pending_documents(request):
    query_set = EmployeeDocuments.objects.filter(
        is_approved=False,
        is_rejected=False,
        is_deleted=False
    )
    print(query_set,"///////////////")
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
    document = EmployeeDocuments.objects.get(pk=pk)
    document.is_rejected=False
    document.is_approved=True
    
    document.save()
    response_data = get_response_data(
        1, redirect_url=reverse("documents:pending_documents"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )



@login_required
def reject_documents(request, pk):
    EmployeeDocuments.objects.filter(pk=pk).update(is_rejected=True, is_approved=False)
    response_data = get_response_data(
        1, redirect_url=reverse("documents:pending_documents"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )