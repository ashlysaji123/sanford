import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from core.functions import generate_form_errors, get_response_data
from .models import Staff
from loans.models import Loan
from salaries.models import SalaryAdavance



class StaffList(ListView):
    template_name = "staffs/list.html"
    queryset = Staff.objects.filter(is_deleted=False)

class StaffDetail(DetailView):
    template_name = "staffs/single.html"
    model = Staff
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = context['object']
        if Loan.objects.filter(is_approved=True,is_returned_completely=False,creator=instance.user).exists():
            loan = Loan.objects.get(is_approved=True,is_returned_completely=False,creator=instance.user)
            context["loan"] = loan
        if SalaryAdavance.objects.filter(is_approved=True,is_returned_completely=False,user=instance.user).exists():
            salary_advance = SalaryAdavance.objects.filter(is_approved=True,is_returned_completely=False,user=instance.user)
            context["salary_advance"] = salary_advance
        return context

