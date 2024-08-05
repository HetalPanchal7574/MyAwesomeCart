from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shopname"),
    path("about/",views.about,name="about"),
    path("contact",views.contact,name="Contact"),
    path("tracker/",views.tracker,name="tracker"),
    path("search",views.search,name="search"),
    path("products/<int:myid>",views.products,name="productview"),
    path("checkout",views.checkout,name="checkout"),
]