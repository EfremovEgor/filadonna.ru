from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("kontakty", views.contacts, name="contacts"),
    path("pravila", views.rules, name="rules"),
    path(
        "dostavka-i-oplata", views.delievery_and_payment, name="delievery_and_payment"
    ),
]
