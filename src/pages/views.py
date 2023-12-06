from django.shortcuts import render
from .models import IndexSliderImage, IndexTileImage


def index(request):
    slider_images = IndexSliderImage.objects.all()
    tiles = IndexTileImage.objects.all()
    return render(
        request,
        "pages/index.html",
        {
            "title": "Купить пряжу из Италии в интернет-магазине с доставкой по России",
            "slider": slider_images,
            "tiles": tiles,
        },
    )


def contacts(request):
    return render(
        request,
        "pages/contacts.html",
        {
            "title": "Контакты",
        },
    )


def rules(request):
    return render(
        request,
        "pages/rules.html",
        {
            "title": "Правила",
        },
    )


def delievery_and_payment(request):
    return render(
        request,
        "pages/delievery_and_payment.html",
        {
            "title": "Доставка и оплата",
        },
    )
