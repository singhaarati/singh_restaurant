from turtle import update
from django.urls import path
from customer import views
urlpatterns=[
    path("",views.index),
    path("create",views.create),
    path("save",views.saveFn),
    path("edit/<int:id>",views.edit),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.delete),
]