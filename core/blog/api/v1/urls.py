from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('post/', views.postlist, name="post-list" ),
    path('post/<int:id>', views.postdetail, name="post-detail" ),
]