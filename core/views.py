import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from coordinators.models import SalesCoordinator, SalesManager
from globalstaffs.models import GlobalManager
from core.functions import generate_form_errors, get_response_data
from core.models import SubRegion, Language, Region, Shop, Area, Year,LocalArea,Company
from executives.models import SalesSupervisor


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

#Company
class CompanyList(ListView):
    queryset = Company.objects.filter(is_deleted=False)


class CompanyDetail(DetailView):
    model = Company


class CompanyForm(CreateView):
    model = Company
    fields = ["region","name","gst","address"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Company"
        return context


class CompanyUpdate(UpdateView):
    model = Company
    fields = ["region","name","gst","address"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Company -"
        return context


class CompanyDelete(DeleteView):
    model = Company
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:company_list")


class LanguageList(ListView):
    queryset = Language.objects.filter(is_deleted=False)


class LanguageDetail(DetailView):
    model = Language


class LanguageForm(CreateView):
    model = Language
    fields = ["name","family","native_name","lang_code"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Language"
        return context


class LanguageUpdate(UpdateView):
    model = Language
    fields = ["name","family","native_name","lang_code"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Language -"
        return context


class LanguageDelete(DeleteView):
    model = Language
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:language_list")


class SubRegionList(ListView):
    template_name = "core/country_list.html"
    queryset = SubRegion.objects.filter(is_deleted=False)


class SubRegionDetail(DetailView):
    template_name = "core/country_detail.html"
    model = SubRegion


class SubRegionForm(CreateView):
    template_name = "core/country_form.html"
    model = SubRegion
    fields = ["name","sub_region_code","region","sub_region_type"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New SubRegion"
        return context


class SubRegionUpdate(UpdateView):
    template_name = "core/country_form.html"
    model = SubRegion
    fields = ["name","sub_region_code","region","sub_region_type"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit SubRegion -"
        return context


class SubRegionDelete(DeleteView):
    model = SubRegion
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:sub_region_list")


class ShopList(ListView):
    queryset = Shop.objects.filter(is_deleted=False)
    def get_queryset(self,**kwargs):
        if self.request.user.is_superuser or self.request.user.is_global_manager:
            queryset = Shop.objects.filter(is_deleted=False)
        else:
            queryset = Shop.objects.filter(is_deleted=False,area__sub_region__region=self.request.user.region)
        return queryset
            


class ShopDetail(DetailView):
    model = Shop


class ShopForm(CreateView):
    model = Shop
    fields = ["name","location", "contact_number", "contact_number2", "area","local_area"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Shop"
        return context


class ShopUpdate(UpdateView):
    model = Shop
    fields = ["name","location", "contact_number", "contact_number2","area","local_area"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Shop -"
        return context


class ShopDelete(DeleteView):
    model = Shop
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:shop_list")


class AreaList(ListView):
    template_name = "core/state_list.html"
    queryset = Area.objects.filter(is_deleted=False)


class AreaDetail(DetailView):
    template_name = "core/state_detail.html"
    model = Area


class AreaForm(CreateView):
    template_name = "core/state_form.html"
    model = Area
    fields = ["name", "sub_region", "area_code"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Area"
        return context


class AreaUpdate(UpdateView):
    model = Area
    fields = ["name", "sub_region", "area_code"]
    template_name = "core/state_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Area -"
        return context


class AreaDelete(DeleteView):
    model = Area
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:area_list")

# Local  area
class LocalAreaList(ListView):
    template_name = "core/local_area_list.html"
    queryset = LocalArea.objects.filter(is_deleted=False)


class LocalAreaDetail(DetailView):
    template_name = "core/local_area_detail.html"
    model = LocalArea


class LocalAreaForm(CreateView):
    template_name = "core/local_area_form.html"
    model = LocalArea
    fields = ["name","area","local_area_code"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Area"
        return context


class LocalAreaUpdate(UpdateView):
    model = LocalArea
    fields = ["name","area", "local_area_code"]
    template_name = "core/local_area_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Area -"
        return context


class LocalAreaDelete(DeleteView):
    model = Area
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:local_area_list")


@login_required
def my_profile(request):
    if request.user.is_global_manager:
        instance = GlobalManager.objects.get(user=request.user)
        context = {"title": "Global manager :- " + instance.name, "instance": instance}
        return render(request, "global-manager/single.html", context)
    if request.user.is_sales_manager:
        instance = SalesManager.objects.get(user=request.user)
        context = {"title": "Sales manager :- " + instance.name, "instance": instance}
        return render(request, "manager/single.html", context)
    elif request.user.is_sales_coordinator:
        instance = SalesCoordinator.objects.get(user=request.user)
        context = {
            "title": "Sales Coordinator :- " + instance.name,
            "instance": instance,
        }
        return render(request, "coordinator/single.html", context)
    elif request.user.is_sales_supervisor:
        instance = SalesSupervisor.objects.get(user=request.user)
        context = {
            "title": "Sales Coordinator :- " + instance.name,
            "instance": instance,
        }
        return render(request, "supervisor/single.html", context)
