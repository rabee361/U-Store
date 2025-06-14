from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("supersecureadmin/", admin.site.urls),
    path("merchant/admin", include("merchant.urls")),
    path("admin/", include("dashboard.urls")),
    path("api/", include("api.urls")),
]
