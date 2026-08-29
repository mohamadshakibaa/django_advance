from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

routers = DefaultRouter()
routers.register('post', views.PostViewSet, basename='post')
urlpatterns = routers.urls

''' Bad az routers dige niazi be in nist
urlpatterns = [
    # path('post/', views.postlist, name="post-list" ),
    # path('post/<int:id>', views.postdetail, name="post-detail" ),
    path('post/', views.PostList.as_view(), name="post-list" ),
    path('post/<int:pk>', views.PostDetail.as_view(), name="post-detail" ),
]'''