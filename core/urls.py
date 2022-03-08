from django.urls import path, re_path

from . import views
from . import superuserviews

app_name = "core"

urlpatterns = [
    # region
    path('add-region', views.add_region, name='add_region'),
    path('region-list', views.region_list, name='region_list'),
    re_path(r'^update-region/(?P<pk>.*)/', views.update_region ,name='update_region'),
    re_path(r'^delete-region/(?P<pk>.*)/', views.delete_region, name='delete_region'),
    # language
    path('add-language', views.add_language, name='add_language'),
    path('language-list', views.language_list, name='language_list'),
    re_path(r'^update-language/(?P<pk>.*)/', views.update_language ,name='update_language'),
    re_path(r'^delete-language/(?P<pk>.*)/', views.delete_language, name='delete_language'),
    # country
    path('add-country', views.add_country, name='add_country'),
    path('country-list', views.country_list, name='country_list'),
    re_path(r'^update-country/(?P<pk>.*)/', views.update_country ,name='update_country'),
    re_path(r'^delete-country/(?P<pk>.*)/', views.delete_country, name='delete_country'),
    # State
    path('add-state', views.add_state, name='add_state'),
    path('state-list', views.state_list, name='state_list'),
    re_path(r'^update-state/(?P<pk>.*)/', views.update_state ,name='update_state'),
    re_path(r'^delete-state/(?P<pk>.*)/', views.delete_state, name='delete_state'),
    # State
    path('add-shop', views.add_shop, name='add_shop'),
    path('shop-list', views.shop_list, name='shop_list'),
    re_path(r'^update-shop/(?P<pk>.*)/', views.update_shop ,name='update_shop'),
    re_path(r'^delete-shop/(?P<pk>.*)/', views.delete_shop, name='delete_shop'),

    # Dashbord urlpatterns
    path('last-month-sales', superuserviews.last_month_sales, name='last_month_sales'),
    path('my-profile', views.my_profile, name='my_profile'),
    


]
