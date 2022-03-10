import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import RewardPoint

# Create your views here.


@login_required
def reward_list(request):
    today = datetime.datetime.now().date()
    month = today.month
    year = today.year
    query_set = RewardPoint.objects.filter(is_deleted=False, year=year, month=month)
    context = {
        "is_need_datatable": True,
        "title": "Reward list",
        "instances": query_set,
    }
    return render(request, "reward/list.htm", context)
