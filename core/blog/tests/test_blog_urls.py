from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from ..views import IndexView, PostDetailView, PostListView


class TestUrl(SimpleTestCase):

    def test_blog_index_url_resolve(self):
        url = reverse("blog:index")
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_blog_post_url_resolve(self):
        url = reverse("blog:post-list")
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_blog_detail_url_resolve(self):
        url = reverse("blog:post-detail", kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
