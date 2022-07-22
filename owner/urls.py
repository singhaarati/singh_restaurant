from django.urls import path
from customer.views import create
from owner import views
urlpatterns = [
    path("o_login/",views.owner_login),
    path("o_register/",views.owner_register),
    path("",views.index),
    path("o_post/",views.owner_post),
    path("save",views.save)
]

