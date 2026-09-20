from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime

from ..models import Post
from accounts.models import User

class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="test@test.com", password="M@123456")
        self.post = Post.objects.create(
            author=self.user,
            title="test",
            content="descriptions",
            category=None,
            status=True,
            published_date=datetime.now(),
        )
        
    def test_blog_index_url_seccessful_response(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # for finding a specefic word in content
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(response, template_name = "index2.html")
        
    def test_blog_post_detail_logged_in_response(self):
        # for login we can use (force_login)
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs={"pk":self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_blog_post_detail_anonymouse_response(self):
        url = reverse("blog:post-detail", kwargs={"pk":self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)