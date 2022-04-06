from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "products"

urlpatterns = [
    # Product category
    path(
        "create-product_category",
        views.create_product_category,
        name="create_product_category",
    ),
    path(
        "product_category-list",
        views.product_category_list,
        name="product_category_list",
    ),
    path(
        "update-product_category/<str:pk>/",
        views.update_product_category,
        name="update_product_category",
    ),
    path(
        "delete-product_category/<str:pk>/",
        views.delete_product_category,
        name="delete_product_category",
    ),
    # category group
    path("category-group/", login_required(views.CategoryGroupList.as_view()), name="category_group_list"),
    path("new/category-group/", views.create_product_category_group, name="new_category_group"),
    path("view/category-group/<str:pk>/", login_required(views.CategoryGroupDetail.as_view()), name="view_category_group",),
    path("update/category-group/<str:pk>/", views.update_product_category_group, name="update_category_group",),
    path("delete/category-group/<str:pk>/", login_required(views.CategoryGroupDelete.as_view()), name="delete_category_group",),
    # Product sub category
    path(
        "create-product_sub_category",
        views.create_product_sub_category,
        name="create_product_sub_category",
    ),
    path(
        "product_sub_category-list",
        views.product_sub_category_list,
        name="product_sub_category_list",
    ),
    path(
        "update-product_sub_category/<str:pk>/",
        views.update_product_sub_category,
        name="update_product_sub_category",
    ),
    path(
        "delete-product_sub_category/<str:pk>/",
        views.delete_product_sub_category,
        name="delete_product_sub_category",
    ),
    # Shop group
    path("shop-group/", login_required(views.ShopGroupList.as_view()), name="shop_group_list"),
    path("new/shop-group/", login_required(views.ShopGroupForm.as_view()), name="new_shop_group"),
    path("view/shop-group/<str:pk>/", login_required(views.ShopGroupDetail.as_view()), name="view_shop_group",),
    path("update/shop-group/<str:pk>/", login_required(views.ShopGroupUpdate.as_view()), name="update_shop_group",),
    path("delete/shop-group/<str:pk>/", login_required(views.ShopGroupDelete.as_view()), name="delete_shop_group",),
    
    # Product
    path("create-product", views.create_product, name="create_product"),
    path("product-list", views.product_list, name="product_list"),
    path("single-product/<str:pk>/", views.product_single, name="product_single"),
    path("update-product/<str:pk>/", views.update_product, name="update_product"),
    path("delete-product/<str:pk>/", views.delete_product, name="delete_product"),

    #Product special price
    path("specialprice/list/", login_required(views.ProductSpecialPriceList.as_view()), name="special_price_list"),
    path("create/specialprice/", login_required(views.ProductSpecialPriceForm.as_view()), name="add_special_price"),
    path("view/specialprice/<str:pk>/", login_required(views.ProductSpecialPriceDetail.as_view()), name="view_special_price",),
    path("update/specialprice/<str:pk>/", login_required(views.ProductSpecialPriceUpdate.as_view()), name="update_special_price",),
    path("delete/specialprice/<str:pk>/", login_required(views.ProductSpecialPriceDelete.as_view()), name="delete_special_price",),
]
