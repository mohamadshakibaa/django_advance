from django.test import TestCase
from datetime import datetime

from ..models import Post
from accounts.models import Profile, User

class TestPostModel(TestCase):
    
    def test_create_post_with_valid_date(self):
        user = User.objects.create_user(email="test@test.com", password="M@123456")
        post = Post.objects.create(
            author = user,
            title ="test",
            content ="descriptions",
            category = None ,
            status = True,
            published_date = datetime.now(),
        )
        self.assertEqual(post.title, "test")