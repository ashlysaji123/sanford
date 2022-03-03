from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
import datetime
from core.functions import generate_form_errors, get_response_data
import json
import sys

from .models import *
# Create your views here.



@login_required
def reward_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    query_set = RewardPoint.objects.filter(is_deleted=False,year=year,month=month)
    context = {
        "is_need_datatable": True,
        "title": "Reward list",
        "instances": query_set
    }
    return render(request, 'reward/list.htm', context)

