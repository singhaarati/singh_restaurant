from django.urls import path
from owner import views
urlpatterns = [
    path("o_login/",views.owner_login),
    path("o_register/",views.owner_register)
]
