from django.test import TestCase
from datetime import datetime

from ..models import Post
from accounts.models import Profile, User


class TestPostModel(TestCase):
    def setUp(self):
        # To avoid repeating it in every test, you can define it once and reuse it in any test.
        self.user = User.objects.create_user(email="test@test.com", password="M@123456")

    def test_create_post_with_valid_date(self):

        post = Post.objects.create(
            author=self.user,
            title="test",
            content="descriptions",
            category=None,
            status=True,
            published_date=datetime.now(),
        )

        self.assertEqual(post.title, "test")
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
