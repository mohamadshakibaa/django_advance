from django.urls import include, path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("tasks/", views.send_email, name="send-email"),
    path("test/", views.test, name="test"),
]
