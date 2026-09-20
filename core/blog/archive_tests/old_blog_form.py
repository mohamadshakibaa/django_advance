from django.test import TestCase, SimpleTestCase
from datetime import datetime

from ..models import Category
from ..forms import PostForm


class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name="hello")
        form = PostForm(data={
            "title":"test",
            "content":"descriptions",
            "category": category_obj ,
            "status": True,
            "published_date": datetime.now(),
        })
        self.assertTrue(form.is_valid())
        
    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())