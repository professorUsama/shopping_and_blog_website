from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrakingStatus"),
    path("search/", views.search, name="Search"),
    path("product/<int:productid>/", views.product, name="Product"),
    path("checkout/", views.checkout, name="CheckOut"),
]
