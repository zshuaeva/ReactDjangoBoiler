# mainpage/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import get_all_photos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/get-all-photos/", get_all_photos, name="get_all_photos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
