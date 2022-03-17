from django.urls import path

from . import views


app_name = "votings"

urlpatterns = [
    path("create-voting", views.create_voting, name="create_voting"),
    path("voting-list", views.voting_list, name="voting_list"),

    path(
        "single-voting/<str:pk>/",
        views.voting_single,
        name="voting_single",
    ),
    
    path(
        "delete_voting/<str:pk>/",
        views.delete_voting,
        name="delete_voting",
    ),
]
