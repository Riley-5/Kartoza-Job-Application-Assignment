from django.urls import path
from portfolio_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
]