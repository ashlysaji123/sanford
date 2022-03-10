from django.urls import path

from . import views

app_name = "rewards"

urlpatterns = [
    path("reward-list", views.reward_list, name="reward_list"),
]
