from django.urls import path

from . import views

urlpatterns = [
    path("add", views.add_predict),
    path("list", views.list_predicts),
    path("login", views.login),
    path("register", views.register)
]
