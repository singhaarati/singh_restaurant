import site
from django.urls import path,include
from django.contrib import admin
urlpatterns = [
    path("",include("home.urls")),
    path("user", include("user.urls")),
    path("product/",include("product.urls")),
    path("owner/",include("owner.urls")),
    path("customer/",include("customer.urls")),
    path("admin/",admin.site.urls)
]
