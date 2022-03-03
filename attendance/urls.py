from django.urls import path, re_path

from . import views

app_name = "attendance"

urlpatterns = [

    path('get-regions',views.get_regions, name='get_regions'),
    
    path('attendance/register-book/',views.register_book,name='register_book'),
    path('attendance/register/page/date/',views.register_page_date,name='register_page_date'),
    path('attendance/register-book/page/',views.register_page,name='register_page'),

    
]
