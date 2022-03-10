from django.urls import path, re_path

from . import views

app_name = "sales"

urlpatterns = [
    # Opening stock
    path(
        "create-opening-stock", views.create_opening_stock, name="create_opening_stock"
    ),
    path("opening-stock-list", views.opening_stock_list, name="opening_stock_list"),
    re_path(
        r"^update-opening-stock/(?P<pk>.*)/",
        views.update_opening_stock,
        name="update_opening_stock",
    ),
    re_path(
        r"^delete-opening-stock/(?P<pk>.*)/",
        views.delete_opening_stock,
        name="delete_opening_stock",
    ),
    path("total-sales-list", views.total_sales, name="total_sales"),
    re_path(r"^sale-single/(?P<pk>.*)/", views.sales_single, name="sales_single"),
    path("pending-sales", views.pending_sales_requests, name="pending_sales_requests"),
    re_path(
        r"^pending-sale-single/(?P<pk>.*)/",
        views.sales_single_pending,
        name="sales_single_pending",
    ),
    re_path(r"^accept-sale/(?P<pk>.*)/", views.accept_sales, name="accept_sales"),
    re_path(r"^reject-sale/(?P<pk>.*)/", views.reject_sales, name="reject_sales"),
]
