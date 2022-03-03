from django.urls import path, re_path

from . import views

app_name = "products"

urlpatterns = [

    # Product category
    path('create-product_category', views.create_product_category, name='create_product_category'),
    path('product_category-list', views.product_category_list, name='product_category_list'),
    re_path(r'^update-product_category/(?P<pk>.*)/', views.update_product_category ,name='update_product_category'),
    re_path(r'^delete-product_category/(?P<pk>.*)/', views.delete_product_category, name='delete_product_category'),
    # Product sub category
    path('create-product_sub_category', views.create_product_sub_category, name='create_product_sub_category'),
    path('product_sub_category-list', views.product_sub_category_list, name='product_sub_category_list'),
    re_path(r'^update-product_sub_category/(?P<pk>.*)/', views.update_product_sub_category ,name='update_product_sub_category'),
    re_path(r'^delete-product_sub_category/(?P<pk>.*)/', views.delete_product_sub_category, name='delete_product_sub_category'),
    # Product sub category
    path('create-product_group', views.create_product_group, name='create_product_group'),
    path('product_group-list', views.product_group_list, name='product_group_list'),
    re_path(r'^update-product_group/(?P<pk>.*)/', views.update_product_group ,name='update_product_group'),
    re_path(r'^delete-product_group/(?P<pk>.*)/', views.delete_product_group, name='delete_product_group'),
    # Product
    path('create-product', views.create_product, name='create_product'),
    path('product-list', views.product_list, name='product_list'),
    re_path(r'^single-product/(?P<pk>.*)/', views.product_single ,name='product_single'),
    re_path(r'^update-product/(?P<pk>.*)/', views.update_product ,name='update_product'),
    re_path(r'^delete-product/(?P<pk>.*)/', views.delete_product, name='delete_product'),

]
