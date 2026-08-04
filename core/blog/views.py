from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm

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


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "category", "status", "published_date"]
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    form_post = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)
