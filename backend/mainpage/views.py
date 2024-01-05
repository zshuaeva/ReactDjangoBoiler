from django.shortcuts import render
from django.http import JsonResponse
from .models import Item


def get_all_photos(request):
    items = Item.objects.all().values("name", "description", "price", "photo")

    data = {
        "items": [
            {
                "name": item["name"],
                "description": item["description"],
                "price": item["price"],
                "photo": item["photo"],
            }
            for item in items
            if item["photo"]
        ]
    }

    return JsonResponse(data, safe=False)
