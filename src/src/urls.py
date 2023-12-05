from django.contrib import admin
from django.urls import include, path, re_path
from . import settings
from django.views.static import serve
from django.conf.urls.static import static

static_urlpatterns = [
    re_path(
        r"^static/(?P<path>.*)$",
        serve,
        {"document_root": settings.STATIC_ROOT},
    ),
]
urlpatterns = [
    path("", include(static_urlpatterns)),
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
