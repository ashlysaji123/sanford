import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from coordinators.models import SalesCoordinator, SalesManager
from core.functions import generate_form_errors, get_response_data
from core.models import Country, Language, Region, Shop, State, Year
from executives.models import SalesExecutive


class YearList(ListView):
    queryset = Year.objects.filter(is_deleted=False)


class YearDetail(DetailView):
    model = Year


class YearForm(CreateView):
    model = Year
    fields = ["name"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Year"
        return context


class YearUpdate(UpdateView):
    model = Year
    fields = ["name"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Year -"
        return context


class YearDelete(DeleteView):
    model = Year
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:year_list")


class RegionList(ListView):
    queryset = Region.objects.filter(is_deleted=False)


class RegionDetail(DetailView):
    model = Region


class RegionForm(CreateView):
    model = Region
    fields = ["name"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Region"
        return context


class RegionUpdate(UpdateView):
    model = Region
    fields = ["name"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Region -"
        return context


class RegionDelete(DeleteView):
    model = Region
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:region_list")


class LanguageList(ListView):
    queryset = Language.objects.filter(is_deleted=False)


class LanguageDetail(DetailView):
    model = Language


class LanguageForm(CreateView):
    model = Language
    fields = ["family","native_name","lang_code"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Language"
        return context


class LanguageUpdate(UpdateView):
    model = Language
    fields = ["family","native_name","lang_code"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Language -"
        return context


class LanguageDelete(DeleteView):
    model = Language
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:language_list")


class CountryList(ListView):
    queryset = Country.objects.filter(is_deleted=False)


class CountryDetail(DetailView):
    model = Country


class CountryForm(CreateView):
    model = Country
    fields = ["name","country_code","region"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Country"
        return context


class CountryUpdate(UpdateView):
    model = Country
    fields = ["name","country_code","region"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Country -"
        return context


class CountryDelete(DeleteView):
    model = Country
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:country_list")


class ShopList(ListView):
    queryset = Shop.objects.filter(is_deleted=False)


class ShopDetail(DetailView):
    model = Shop


class ShopForm(CreateView):
    model = Shop
    fields = ["name","location", "contact_number", "contact_number2", "country", "state"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Shop"
        return context


class ShopUpdate(UpdateView):
    model = Shop
    fields = ["name","location", "contact_number", "contact_number2", "country", "state"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Shop -"
        return context


class ShopDelete(DeleteView):
    model = Shop
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:shop_list")


class StateList(ListView):
    queryset = State.objects.filter(is_deleted=False)


class StateDetail(DetailView):
    model = State


class StateForm(CreateView):
    model = State
    fields = ["name","type", "country", "state_code", "tin_number"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New State"
        return context


class StateUpdate(UpdateView):
    model = State
    fields = ["name","type", "country", "state_code", "tin_number"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit State -"
        return context


class StateDelete(DeleteView):
    model = State
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:state_list")


@login_required
def my_profile(request):
    if request.user.salesmanager:
        instance = SalesManager.objects.get(user=request.user)
        context = {"title": "Sales manager :- " + instance.name, "instance": instance}
        return render(request, "manager/single.html", context)
    elif request.user.salescoordinator:
        instance = SalesCoordinator.objects.get(user=request.user)
        context = {
            "title": "Sales Coordinator :- " + instance.name,
            "instance": instance,
        }
        return render(request, "coordinator/single.html", context)
    elif request.user.salesexecutive:
        instance = SalesExecutive.objects.get(user=request.user)
        context = {"title": "Sales Executive :- " + instance.name, "instance": instance}
        return render(request, "executive/single.html", context)
