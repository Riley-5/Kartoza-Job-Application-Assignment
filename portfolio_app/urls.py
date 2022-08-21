from django.urls import path
from portfolio_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("map", views.map, name="map"),
    path("get_users", views.get_users, name="get_users"),
]