import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from core.functions import generate_form_errors, get_response_data
from .models import Staff



class StaffList(ListView):
    template_name = "staffs/list.html"
    queryset = Staff.objects.filter(is_deleted=False)

class StaffDetail(DetailView):
    template_name = "staffs/single.html"
    model = Staff
