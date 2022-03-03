from django.urls import path, re_path

from . import views

app_name = "rewards"

urlpatterns = [
    path('reward-list', views.reward_list, name='reward_list'),
    
]
