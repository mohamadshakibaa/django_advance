from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    # path('post/', views.postlist, name="post-list" ),
    # path('post/<int:id>', views.postdetail, name="post-detail" ),
    path('post/', views.PostList.as_view(), name="post-list" ),
    path('post/<int:id>', views.PostDetail.as_view(), name="post-detail" ),
]