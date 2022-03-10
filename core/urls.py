from django.contrib.auth.decorators import login_required
from django.urls import path

from . import superuserviews, views

app_name = "core"

urlpatterns = [
    # Years
    path("years/", login_required(views.YearList.as_view()), name="year_list"),
    path("new/year/", login_required(views.YearForm.as_view()), name="new_year"),
    path("view/year/<str:pk>/", login_required(views.YearDetail.as_view()), name="view_year",),
    path("update/year/<str:pk>/", login_required(views.YearUpdate.as_view()), name="update_year",),
    path("delete/year/<str:pk>/", login_required(views.YearDelete.as_view()), name="delete_year",),
    # Regions
    path("regions/", login_required(views.RegionList.as_view()), name="region_list"),
    path("new/region/", login_required(views.RegionForm.as_view()), name="new_region"),
    path("view/region/<str:pk>/", login_required(views.RegionDetail.as_view()), name="view_region",),
    path("update/region/<str:pk>/", login_required(views.RegionUpdate.as_view()), name="update_region",),
    path("delete/region/<str:pk>/", login_required(views.RegionDelete.as_view()), name="delete_region",),
    # Languages
    path("languages/", login_required(views.LanguageList.as_view()), name="language_list"),
    path("new/language/", login_required(views.LanguageForm.as_view()), name="new_language",),
    path("view/language/<str:pk>/", login_required(views.LanguageDetail.as_view()), name="view_language",),
    path("update/language/<str:pk>/", login_required(views.LanguageUpdate.as_view()), name="update_language",),
    path("delete/language/<str:pk>/", login_required(views.LanguageDelete.as_view()), name="delete_language",),
    # Countrys
    path("countries/", login_required(views.CountryList.as_view()), name="country_list"),
    path("new/country/", login_required(views.CountryForm.as_view()), name="new_country"),
    path("view/country/<str:pk>/", login_required(views.CountryDetail.as_view()), name="view_country",),
    path("update/country/<str:pk>/", login_required(views.CountryUpdate.as_view()), name="update_country",),
    path("delete/country/<str:pk>/", login_required(views.CountryDelete.as_view()), name="delete_country",),
    # Shops
    path("shops/", login_required(views.ShopList.as_view()), name="shop_list"),
    path("new/shop/", login_required(views.ShopForm.as_view()), name="new_shop"),
    path("view/shop/<str:pk>/", login_required(views.ShopDetail.as_view()), name="view_shop",),
    path("update/shop/<str:pk>/", login_required(views.ShopUpdate.as_view()), name="update_shop",),
    path("delete/shop/<str:pk>/", login_required(views.ShopDelete.as_view()), name="delete_shop",),
    # States
    path("states/", login_required(views.StateList.as_view()), name="state_list"),
    path("new/state/", login_required(views.StateForm.as_view()), name="new_state"),
    path("view/state/<str:pk>/", login_required(views.StateDetail.as_view()), name="view_state",),
    path("update/state/<str:pk>/", login_required(views.StateUpdate.as_view()), name="update_state",),
    path("delete/state/<str:pk>/", login_required(views.StateDelete.as_view()), name="delete_state",),
    # Dashbord urlpatterns
    path("last-month-sales", superuserviews.last_month_sales, name="last_month_sales"),
    path("my-profile", views.my_profile, name="my_profile"),
]
