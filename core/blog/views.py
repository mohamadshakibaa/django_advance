from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def indexView(request):
    """
    a function based view to show index page
    """
    return render(request, 'index.html')


class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = "index2.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'  # example
        return context
    