import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from coordinators.models import SalesCoordinator, SalesManager
from core.forms import CountryForm, LanguageForm, RegionForm, ShopForm, StateForm
from core.functions import generate_form_errors, get_response_data
from core.models import Country, Language, Region, Shop, State
from executives.models import SalesExecutive

"""Region"""


@login_required
def add_region(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("core:region_list"),
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
        form = RegionForm()
        context = {"form": form, "title": "Add Region", "alert_type": "showalert"}
        return render(request, "core/region/create.html", context)


@login_required
def region_list(request):
    query_set = Region.objects.filter(is_deleted=False)
    context = {"title": "Regions", "instances": query_set}
    return render(request, "core/region/list.html", context)


@login_required
def update_region(request, pk):
    instance = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        form = RegionForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("core:region_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = RegionForm(instance=instance)
        context = {"title": "Edit Region", "form": form, "instance": instance}
        return render(request, "core/region/create.html", context)


@login_required
def delete_region(request, pk):
    Region.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("core:region_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Region"""


"""Language"""


@login_required
def add_language(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("core:language_list"),
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
        form = LanguageForm()
        context = {"form": form, "title": "Add Language", "alert_type": "showalert"}
        return render(request, "core/language/create.html", context)


@login_required
def language_list(request):
    query_set = Language.objects.filter(is_deleted=False)
    context = {"title": "Language", "instances": query_set}
    return render(request, "core/language/list.html", context)


@login_required
def update_language(request, pk):
    instance = get_object_or_404(Language, pk=pk)
    if request.method == "POST":
        form = LanguageForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("core:language_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = LanguageForm(instance=instance)
        context = {"title": "Edit language", "form": form, "instance": instance}
        return render(request, "core/language/create.html", context)


@login_required
def delete_language(request, pk):
    Language.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("core:language_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""language"""


"""country"""


@login_required
def add_country(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("core:country_list"),
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
        form = CountryForm()
        context = {"form": form, "title": "Add Country", "alert_type": "showalert"}
        return render(request, "core/country/create.html", context)


@login_required
def country_list(request):
    query_set = Country.objects.filter(is_deleted=False)
    context = {"title": "Country", "instances": query_set}
    return render(request, "core/country/list.html", context)


@login_required
def update_country(request, pk):
    instance = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("core:country_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = CountryForm(instance=instance)
        context = {"title": "Edit Country", "form": form, "instance": instance}
        return render(request, "core/country/create.html", context)


@login_required
def delete_country(request, pk):
    Country.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("core:country_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""country"""


"""State"""


@login_required
def add_state(request):
    if request.method == "POST":
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("core:state_list"),
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
        form = StateForm()
        context = {"form": form, "title": "Add State", "alert_type": "showalert"}
        return render(request, "core/state/create.html", context)


@login_required
def state_list(request):
    query_set = State.objects.filter(is_deleted=False)
    context = {"title": "State", "instances": query_set}
    return render(request, "core/state/list.html", context)


@login_required
def update_state(request, pk):
    instance = get_object_or_404(State, pk=pk)
    if request.method == "POST":
        form = StateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("core:state_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = StateForm(instance=instance)
        context = {"title": "Edit State", "form": form, "instance": instance}
        return render(request, "core/state/create.html", context)


@login_required
def delete_state(request, pk):
    State.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("core:state_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""State"""


"""Shop"""


@login_required
def add_shop(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("core:shop_list"), message="Added Successfully."
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
        form = ShopForm()
        context = {"form": form, "title": "Add Shop", "alert_type": "showalert"}
        return render(request, "core/shop/create.html", context)


@login_required
def shop_list(request):
    if request.user.is_superuser:
        query_set = Shop.objects.filter(is_deleted=False)
    else:
        query_set = Shop.objects.filter(
            is_deleted=False, country__region=request.user.region
        )
    context = {"title": "Shop", "instances": query_set}
    return render(request, "core/shop/list.html", context)


@login_required
def update_shop(request, pk):
    instance = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("core:shop_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = ShopForm(instance=instance)
        context = {"title": "Edit Shop", "form": form, "instance": instance}
        return render(request, "core/shop/create.html", context)


@login_required
def delete_shop(request, pk):
    Shop.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("core:shop_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Shop"""


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
