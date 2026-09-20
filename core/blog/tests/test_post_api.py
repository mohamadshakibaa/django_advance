from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime

from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def commen_user():
    user = User.objects.create_user(
        email="admin@admin.com", password="m@123456", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_post_create_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "descriptions",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_post_create_response_201_status(self, api_client, commen_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "descriptions",
            "status": True,
            "published_date": datetime.now(),
        }
        api_client.force_login(commen_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_post_invalid_data_response_400_status(self, api_client, commen_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "descriptions",
        }
        api_client.force_login(commen_user)
        response = api_client.post(url, data)
        assert response.status_code == 400
