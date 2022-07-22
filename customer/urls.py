from turtle import update
from django.urls import path
from customer import views
urlpatterns=[
    path("",views.index, name="customer_index"),
    path("create",views.create, name="customer_create"),
    path("save",views.saveFn,name="customer_saveFn"),
    path("edit/<int:id>",views.edit,name="customer_edit"),
    path("update/<int:id>",views.update,name="customer_update"),
    path("delete/<int:id>",views.delete,name="customer_delete"),
]