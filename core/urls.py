from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns as swagger_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.products.urls")),
]
urlpatterns += swagger_patterns
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
