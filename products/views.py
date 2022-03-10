import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data

from .forms import CategoryForm, ProductForm, ProductGroupForm, SubCategoryForm
from .models import Category, Product, ProductGroup, SubCategory

# Create your views here.


"""Product category"""


@login_required
def create_product_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:product_category_list"),
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
        form = CategoryForm()
        context = {"form": form, "title": "Add Category", "alert_type": "showalert"}
        return render(request, "product/category/create.html", context)


@login_required
def product_category_list(request):
    query_set = Category.objects.filter(is_deleted=False)
    context = {
        "title": "Category list",
        "instances": query_set,
    }
    return render(request, "product/category/list.html", context)


@login_required
def update_product_category(request, pk):
    instance = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:product_category_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = CategoryForm(instance=instance)
        context = {"title": "Edit Product Category", "form": form, "instance": instance}
        return render(request, "product/category/create.html", context)


@login_required
def delete_product_category(request, pk):
    Category.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("products:product_category_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Product category"""


"""Produc subt category"""


@login_required
def create_product_sub_category(request):
    if request.method == "POST":
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:product_sub_category_list"),
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
        form = SubCategoryForm()
        context = {"form": form, "title": "Add Sub Category", "alert_type": "showalert"}
        return render(request, "product/subcategory/create.html", context)


@login_required
def product_sub_category_list(request):
    query_set = SubCategory.objects.filter(is_deleted=False)
    context = {
        "title": "Sub Category list",
        "instances": query_set,
    }
    return render(request, "product/subcategory/list.html", context)


@login_required
def update_product_sub_category(request, pk):
    instance = get_object_or_404(SubCategory, pk=pk)
    if request.method == "POST":
        form = SubCategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:product_sub_category_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = SubCategoryForm(instance=instance)
        context = {
            "title": "Edit Product Sub Category",
            "form": form,
            "instance": instance,
        }
        return render(request, "product/subcategory/create.html", context)


@login_required
def delete_product_sub_category(request, pk):
    SubCategory.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("products:product_sub_category_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Product sub category"""

"""Produc group"""


@login_required
def create_product_group(request):
    if request.method == "POST":
        form = ProductGroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:product_group_list"),
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
        form = ProductGroupForm()
        context = {"form": form, "title": "Add Group", "alert_type": "showalert"}
        return render(request, "product/group/create.html", context)


@login_required
def product_group_list(request):
    query_set = ProductGroup.objects.filter(is_deleted=False)
    context = {"title": "Group list", "instances": query_set}
    return render(request, "product/group/list.html", context)


@login_required
def update_product_group(request, pk):
    instance = get_object_or_404(ProductGroup, pk=pk)
    if request.method == "POST":
        form = ProductGroupForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:product_group_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = ProductGroupForm(instance=instance)
        context = {"title": "Edit Group", "form": form, "instance": instance}
        return render(request, "product/group/create.html", context)


@login_required
def delete_product_group(request, pk):
    ProductGroup.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("products:product_group_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Product group"""


"""Product"""


@login_required
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.save()
            form.save_m2m()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:product_list"),
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
        form = ProductForm()
        context = {"form": form, "title": "Add Product", "alert_type": "showalert"}
        return render(request, "product/create.html", context)


@login_required
def product_list(request):
    query_set = Product.objects.filter(is_deleted=False)
    context = {
        "title": "Product list",
        "instances": query_set,
    }
    return render(request, "product/list.html", context)


@login_required
def product_single(request, pk):
    instance = get_object_or_404(Product, pk=pk)
    available_regions = instance.available_regions.all()

    context = {
        "title": "Product :- " + instance.name,
        "instance": instance,
        "available_regions": available_regions,
    }
    return render(request, "product/single.html", context)


@login_required
def update_product(request, pk):
    instance = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1, redirect_url=reverse("products:product_list"), message="Updated"
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = ProductForm(instance=instance)
        context = {"title": "Edit Product ", "form": form, "instance": instance}
        return render(request, "product/create.html", context)


@login_required
def delete_product(request, pk):
    Product.objects.filter(pk=pk).update(is_deleted=True)
    response_data = get_response_data(
        1, redirect_url=reverse("products:product_list"), message="Deleted"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


"""Product"""
