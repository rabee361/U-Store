from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("supersecureadmin/", admin.site.urls),
    path("merchant/", include("merchant.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/", include("api.urls")),
]
