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
    # sub_region
    path("sub_regions/", login_required(views.SubRegionList.as_view()), name="sub_region_list"),
    path("new/sub_region/", login_required(views.SubRegionForm.as_view()), name="new_sub_region"),
    path("view/sub_region/<str:pk>/", login_required(views.SubRegionDetail.as_view()), name="view_sub_region",),
    path("update/sub_region/<str:pk>/", login_required(views.SubRegionUpdate.as_view()), name="update_sub_region",),
    path("delete/sub_region/<str:pk>/", login_required(views.SubRegionDelete.as_view()), name="delete_sub_region",),
    # Shops
    path("shops/", login_required(views.ShopList.as_view()), name="shop_list"),
    path("new/shop/", login_required(views.ShopForm.as_view()), name="new_shop"),
    path("view/shop/<str:pk>/", login_required(views.ShopDetail.as_view()), name="view_shop",),
    path("update/shop/<str:pk>/", login_required(views.ShopUpdate.as_view()), name="update_shop",),
    path("delete/shop/<str:pk>/", login_required(views.ShopDelete.as_view()), name="delete_shop",),
    # Area
    path("area-list/", login_required(views.AreaList.as_view()), name="area_list"),
    path("new/area/", login_required(views.AreaForm.as_view()), name="new_area"),
    path("view/area/<str:pk>/", login_required(views.AreaDetail.as_view()), name="view_area",),
    path("update/area/<str:pk>/", login_required(views.AreaUpdate.as_view()), name="update_area",),
    path("delete/area/<str:pk>/", login_required(views.AreaDelete.as_view()), name="delete_area",),
    # Local Area
    path("local-area-list/", login_required(views.LocalAreaList.as_view()), name="local_area_list"),
    path("new/local-area/", login_required(views.LocalAreaForm.as_view()), name="new_local_area"),
    path("view/local-area/<str:pk>/", login_required(views.LocalAreaDetail.as_view()), name="view_local_area",),
    path("update/local-area/<str:pk>/", login_required(views.LocalAreaUpdate.as_view()), name="update_local_area",),
    path("delete/local-area/<str:pk>/", login_required(views.LocalAreaDelete.as_view()), name="delete_local_area",),
    # Dashbord urlpatterns
    path("last-month-sales", superuserviews.last_month_sales, name="last_month_sales"),
    path("my-profile", views.my_profile, name="my_profile"),
]
