from django.shortcuts import render
from django.http import JsonResponse
from .models import Item


def get_all_photos(request):
    photos = Item.objects.all().values("photo")
    photo_urls = [photo["photo"] for photo in photos if photo["photo"]]
    return JsonResponse({"photoUrls": photo_urls}, safe=False)
