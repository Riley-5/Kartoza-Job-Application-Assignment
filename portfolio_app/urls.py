from django.urls import path
from portfolio_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("map", views.map, name="map"),
    path("get_users", views.get_users, name="get_users"),
]