from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core import dashboardview as dashboard

from .swagger import schema_view

urlpatterns = (
    [
        path("admin/doc/", include("django.contrib.admindocs.urls")),
        path("admin/", admin.site.urls),
        path(
            "docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
        # registration
        path("accounts/", include("registration.backends.default.urls")),
        # path("", TemplateView.as_view(template_name="core/region/create.html")),
        path("", dashboard.app, name="app"),
        path(
            "api/v1/accounts/",
            include("api.v1.accounts.urls", namespace="api_v1_accounts"),
        ),
        path(
            "api/v1/attendance/",
            include("api.v1.attendance.urls", namespace="api_v1_attendance"),
        ),
        path("api/v1/core/", include("api.v1.core.urls", namespace="api_v1_core")),
        path("api/v1/leave/", include("api.v1.leave.urls", namespace="api_v1_leave")),
        path(
            "api/v1/merchandiser/",
            include("api.v1.merchandiser.urls", namespace="api_v1_merchandiser"),
        ),
        path(
            "api/v1/executives/",
            include("api.v1.executives.urls", namespace="api_v1_executives"),
        ),
        path(
            "api/v1/coordinators/",
            include("api.v1.coordinators.urls", namespace="api_v1_coordinators"),
        ),
        path(
            "api/v1/notifications/",
            include("api.v1.notifications.urls", namespace="api_v1_notifications"),
        ),
        path(
            "api/v1/products/",
            include("api.v1.products.urls", namespace="api_v1_products"),
        ),

        path(
            "api/v1/documents/",
            include("api.v1.documents.urls", namespace="api_v1_documents"),
        ),

        path(
            "api/v1/salaries/",
            include("api.v1.salaries.urls", namespace="api_v1_salaries"),
        ),

        path(
            "api/v1/loans/",
            include("api.v1.loans.urls", namespace="api_v1_loans"),
        ),

        path(
            "api/v1/reports/",
            include("api.v1.reports.urls", namespace="api_v1_reports"),
        ),
        
        path(
            "api/v1/votings/",
            include("api.v1.votings.urls", namespace="api_v1_votings"),
        ),
        path("api/v1/sales/", include("api.v1.sales.urls", namespace="api_v1_sales")),
        path(
            "api/v1/rewards/",
            include("api.v1.rewards.urls", namespace="api_v1_rewards"),
        ),
        path("accounts/", include("accounts.urls", namespace="accounts")),
        path("attendance/", include("attendance.urls", namespace="attendance")),
        path("core/", include("core.urls", namespace="core")),
        path("leave/", include("leave.urls", namespace="leave")),
        path("merchandiser/", include("merchandiser.urls", namespace="merchandiser")),
        path("coordinators/", include("coordinators.urls", namespace="coordinators")),
        path("globalstaffs/", include("globalstaffs.urls", namespace="globalstaffs")),
        path("executives/", include("executives.urls", namespace="executives")),
        path(
            "notifications/", include("notifications.urls", namespace="notifications")
        ),
        path("products/", include("products.urls", namespace="products")),
        path("sales/", include("sales.urls", namespace="sales")),
        path("rewards/", include("rewards.urls", namespace="rewards")),
        path("expenses/", include("expenses.urls", namespace="expenses")),
        path("reports/", include("reports.urls", namespace="reports")),
        path("votings/", include("votings.urls", namespace="votings")),
        path("documents/", include("documents.urls", namespace="documents")),
        path("salaries/", include("salaries.urls", namespace="salaries")),
        path("loans/", include("loans.urls", namespace="loans")),
        path("tinymce/", include("tinymce.urls")),


    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Sanford Corp Administration"
admin.site.site_title = "Sanford Corp Admin Portal"
admin.site.index_title = "Welcome to Sanford Corp Admin Portal"
