import imp
from django.shortcuts import render
import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data

from .forms import VotingItemForm
from .models import VotingItem,Voting

# Create your views here.
@login_required
def create_voting(request):
    if request.method == "POST":
        form = VotingItemForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("votings:voting_list"),
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
        form = VotingItemForm()
        context = {"form": form, "title": "Add voting", "alert_type": "showalert"}
        return render(request, "voting/create.html", context)


@login_required
def voting_list(request):
    current_month = datetime.date.today().month
    query_set = VotingItem.objects.filter(voting_startdate__month=current_month)
    context = {
        "title": "Voting list",
        "instances": query_set,
    }
    return render(request, "voting/list.html", context)


@login_required
def voting_single(request, pk):
    instance = get_object_or_404(VotingItem, pk=pk)
    voting = Voting.objects.filter(voting_item=instance).prefetch_related('voting_item')
    perfect_count = voting.filter(voting="perfect").count()
    good_count = voting.filter(voting="good").count()
    bad_count = voting.filter(voting="bad").count()
    context = {
        "title": "Voting Item", 
        "instance": instance , 
        "voting": voting,
        "perfect_count":perfect_count,
        "good_count":good_count,
        "bad_count":bad_count,
        }
    return render(request, "voting/single.html", context)


@login_required
def delete_voting(request, pk):
    VotingItem.objects.get(pk=pk).delete()
    response_data = get_response_data(
        1, redirect_url=reverse("votings:voting_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )