from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    path("fbv-index", views.indexView),
    path("cbv-index", views.IndexView.as_view(template_name="index2.html")),
    path("go-to-index", RedirectView.as_view(url="http://index2.com")), # example
    path("go-to-index", RedirectView.as_view(pattern_name="blog:index2"), name='cbv_view'), # or we can use   pattern_name

]