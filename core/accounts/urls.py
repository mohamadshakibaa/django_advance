from django.urls import include, path
from .views import send_email

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("tasks/", send_email)
]
