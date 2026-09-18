from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import PostForm
from .models import Post

# Create your views here.


def home(request):
    return render(request, "index.html")


def indexView(request):
    """
    a function based view to show index page
    """
    return render(request, "index.html")


class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "index2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"  # example
        return context


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = "id"
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "category", "status", "published_date"]
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"
