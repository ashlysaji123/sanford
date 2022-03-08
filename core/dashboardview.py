from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
import datetime
from core.functions import generate_form_errors,get_response_data
import json
import sys

from core.forms import *
from core.models import *
from core.functions import get_current_role
from products.models import Product
from notifications.models import Notification
from coordinators.models import SalesManager,SalesCoordinator
from executives.models import SalesExecutive
from merchandiser.models import Merchandiser
from leave.models import LeaveRequest


@login_required
def app(request):
    datetime.date.today()
    role_data = get_current_role(request)
    current_role = None
    if role_data:
        for key, value in role_data.items():
            if key == "role":
                current_role = value
            elif key == "user":
                user = value

    is_superuser = False
    is_sales_manager = False
    is_sales_coordinator = False
    is_sales_executive = False


    notifications = Notification.objects.filter(is_deleted=False)
    notifications_count = notifications.count()
    product_count = Product.objects.filter(is_deleted=False).count()
    hot_products = Product.objects.filter(is_hot_product=True).order_by('-created')[:5]

    if current_role == "superuser":
        is_superuser = True
        manager_count = SalesManager.objects.filter(is_deleted=False).count()
        coordinator_count = SalesCoordinator.objects.filter(is_deleted=False).count()
        executive_count = SalesExecutive.objects.filter(is_deleted=False).count()
        merchandiser_count = Merchandiser.objects.filter(is_deleted=False).count()
        shope_count = Shop.objects.filter(is_deleted=False).count()
    elif current_role == "salesmanager":
        is_sales_manager = True
        coordinator_count = SalesCoordinator.objects.filter(is_deleted=False,region=request.user.region).count()
        executive_count = SalesExecutive.objects.filter(is_deleted=False,region=request.user.region).count()
        merchandiser_count = Merchandiser.objects.filter(is_deleted=False,state__country__region=request.user.region).count()
        pending_leave_request = LeaveRequest.objects.filter(is_deleted=False,is_approved=False,is_rejected=False,user__region=request.user.region).count()
    elif current_role == "salescoordinator":
        is_sales_coordinator = True
    elif current_role == "salesexecutive":
        is_sales_executive = True

    context = {
       "domain" : request.build_absolute_uri('/')[:-1],
        "current_path": request.get_full_path(),
        "site_title": "sanfordcorp Portal",

        "current_role": current_role,
        "is_superuser": is_superuser,
        "is_sales_manager": is_sales_manager,
        "is_sales_coordinator":is_sales_coordinator,
        "is_sales_executive":is_sales_executive,
        "notifications_count":notifications_count,
        "notifications":notifications,
        "product_count":product_count,
        "hot_products": hot_products,
    }
    if current_role == "superuser":
        context.update({
            "merchandiser_count":merchandiser_count,
            "executive_count":executive_count,
            "coordinator_count":coordinator_count,
            "manager_count":manager_count,
            "shope_count":shope_count,
        })
    elif current_role == "salesmanager":
        context.update({
            "merchandiser_count":merchandiser_count,
            "executive_count":executive_count,
            "coordinator_count":coordinator_count,
            "pending_leave_request":pending_leave_request,
        })

    return render(request, "index.html", context)

