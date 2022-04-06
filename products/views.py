import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from core.functions import generate_form_errors, get_response_data

from .forms import CategoryForm, ProductForm, SubCategoryForm,CategoryGroupForm
from .models import Category, Product, ShopGroup, SubCategory,ProductSpecialPrice,CategoryGroup
from core.models import Shop

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

class CategoryGroupList(ListView):
    template_name = "product/category-group/group_list.html"
    queryset = CategoryGroup.objects.filter(is_deleted=False)


class CategoryGroupDetail(DetailView):
    template_name = "product/category-group/group_detail.html"
    model = CategoryGroup



@login_required
def create_product_category_group(request):
    if request.method == "POST":
        form = CategoryGroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:category_group_list"),
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
        form = CategoryGroupForm()
        context = {"form": form, "title": "New Category Group", "alert_type": "showalert"}
        return render(request, "product/category-group/group_form.html", context)



@login_required
def update_product_category_group(request, pk):
    instance = get_object_or_404(CategoryGroup, pk=pk)
    if request.method == "POST":
        form = CategoryGroupForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = get_response_data(
                1,
                redirect_url=reverse("products:category_group_list"),
                message="Updated",
            )
        else:
            message = generate_form_errors(form, formset=False)
            response_data = get_response_data(0, message=message)
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        form = CategoryGroupForm(instance=instance)
        context = {"title": "Edit Category Group -", "form": form, "instance": instance}
        return render(request, "product/category-group/group_form.html", context)



class CategoryGroupDelete(DeleteView):
    model = CategoryGroup
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("products:category_group_list")


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
class ShopGroupList(ListView):
    queryset = ShopGroup.objects.filter(is_deleted=False)
    template_name = "product/group/list.html"
    def get_queryset(self,**kwargs):
        if self.request.user.is_superuser or self.request.user.is_global_manager:
            queryset = ShopGroup.objects.filter(is_deleted=False)
        else:
            queryset = ShopGroup.objects.filter(is_deleted=False,region=self.request.user.region)
        return queryset
            
class ShopGroupDetail(DetailView):
    model = ShopGroup
    template_name = "product/group/single.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = context['object']
        context["shop_list"] = data.shops.all()
        return context

class ShopGroupForm(CreateView):
    model = ShopGroup
    template_name = "product/group/create.html"
    fields = ["name","region", "shops"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Customer Group"
        return context

class ShopGroupUpdate(UpdateView):
    model = ShopGroup
    template_name = "product/group/create.html"
    fields = ["name","region", "shops"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Customer group -"
        return context

class ShopGroupDelete(DeleteView):
    model = ShopGroup
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("products:shop_group_list")

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


""" product special price"""
class ProductSpecialPriceList(ListView):
    queryset = ProductSpecialPrice.objects.filter(is_deleted=False)
    template_name = 'product/specialprice/productspecialprice_list.html'

class ProductSpecialPriceDetail(DetailView):
    model = ProductSpecialPrice
    template_name = 'product/specialprice/productspecialprice_detail.html'

class ProductSpecialPriceForm(CreateView):
    model = ProductSpecialPrice
    fields = ["group","product","special_price"]
    template_name = 'product/specialprice/productspecialprice_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Special Price for Group"
        if self.request.user.is_superuser or self.request.user.is_global_manager:
            qs = ShopGroup.objects.filter(is_deleted=False)
        else:
            qs = ShopGroup.objects.filter(region=self.request.user.region,is_deleted=False)
        form = context['form']
        form_group = form.fields['group']
        form_group.queryset = qs
        return context


class ProductSpecialPriceUpdate(UpdateView):
    model = ProductSpecialPrice
    fields = ["group","product","special_price"]
    template_name = 'product/specialprice/productspecialprice_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Special Price -"
        return context


class ProductSpecialPriceDelete(DeleteView):
    model = ProductSpecialPrice
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("products:special_price_list")
