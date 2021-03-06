from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "sales"

urlpatterns = [
    # Opening stock
    path(
        "create-opening-stock", views.create_opening_stock, name="create_opening_stock"
    ),
    path("opening-stock-list", views.opening_stock_list, name="opening_stock_list"),
    path(
        "update-opening-stock/<str:pk>/",
        views.update_opening_stock,
        name="update_opening_stock",
    ),
    path(
        "delete-opening-stock/<str:pk>/",
        views.delete_opening_stock,
        name="delete_opening_stock",
    ),
    # Sales
    path("total-sales-list", views.total_sales, name="total_sales"),
    path("sale-single/<str:pk>/", views.sales_single, name="sales_single"),
    path("pending-sales", views.pending_sales_requests, name="pending_sales_requests"),
    path(
        "pending-sale-single/<str:pk>/",
        views.sales_single_pending,
        name="sales_single_pending",
    ),
    path("accept-sale/<str:pk>/", views.accept_sales, name="accept_sales"),
    path("reject-sale/<str:pk>/", views.reject_sales, name="reject_sales"),
    # Sale returns
    path("sales/return/list", login_required(views.SaleReturnList.as_view()), name="sales_return_list"),
    path("sale/return/single/<str:pk>/", login_required(views.SaleReturnDetail.as_view()), name="single_sales_return"),


    path("select_satff", views.select_satff_for_reports, name="select_satff_for_reports"),
    path("sales-report", views.sales_report, name="sales_report"),
]
