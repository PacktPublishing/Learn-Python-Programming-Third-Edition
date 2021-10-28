# apic/rails/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "stations", views.StationsView.as_view(), name="stations"
    ),
    path(
        "stations/<int:station_id>/departures",
        views.DeparturesView.as_view(),
        name="departures",
    ),
    path(
        "stations/<int:station_id>/arrivals",
        views.ArrivalsView.as_view(),
        name="arrivals",
    ),
    path("users", views.UsersView.as_view(), name="users"),
    path(
        "authenticate",
        views.AuthenticateView.as_view(),
        name="authenticate",
    ),
    path(
        "authenticate/result",
        views.AuthenticateResultView.as_view(),
        name="auth_result",
    ),
]
