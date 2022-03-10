from django.urls import path

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
    # Product sub category
    path(
        "create-product_group", views.create_product_group, name="create_product_group"
    ),
    path("product_group-list", views.product_group_list, name="product_group_list"),
    path(
        "update-product_group/<str:pk>/",
        views.update_product_group,
        name="update_product_group",
    ),
    path(
        "delete-product_group/<str:pk>/",
        views.delete_product_group,
        name="delete_product_group",
    ),
    # Product
    path("create-product", views.create_product, name="create_product"),
    path("product-list", views.product_list, name="product_list"),
    path("single-product/<str:pk>/", views.product_single, name="product_single"),
    path("update-product/<str:pk>/", views.update_product, name="update_product"),
    path("delete-product/<str:pk>/", views.delete_product, name="delete_product"),
]
