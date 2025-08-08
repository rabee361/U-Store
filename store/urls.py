from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("supersecureadmin/", admin.site.urls),
    path("merchant/", include("merchant.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/", include("api.urls")),
    path("404/", page_not_found , name="404"),
    path("500/", server_error , name="500"),
]

# 📁 Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
