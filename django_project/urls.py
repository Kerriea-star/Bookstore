from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # local apps
    path("", include("pages.urls")),
]
