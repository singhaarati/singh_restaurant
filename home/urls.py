from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name="buy_index"),
    path("buy/",views.buy_page,name="buy_product"),
]
