from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.views import APIView

"""Function Based View 
                                           
@api_view(["GET", "POST"])
@permission_classes([IsAdminUser])
def postlist(request):
    if request.method == 'GET':
        # posts = Post.objects.all()
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

                                          
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def postdetail(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == "DELETE":
        post.delete()
        return Response({"detail": "This item was deleted"}, status=status.HTTP_204_NO_CONTENT)

"""


""" this part is about try/exception in Function Based View  (Not Important)                                                   
@api_view()
def postdetail(request, id):
    # try:                                   instead of Get_Object_or_404
        # post = Post.objects.get(pk=id)
        post = get_object_or_404(Post, pk=id)
        print(post.__dict__)
        serializer = PostSerializer(post)
        print(serializer.data)
        return Response(serializer.data)
    # except Post.DoesNotExist:
        # return Response({"detail":"Post dose not exist"}, status=status.HTTP_404_NOT_FOUND)/
"""


""" Class Based View with  (APIView)  GET, POST
class PostList(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""

""" Class Based View with  (AOIView)  GET, PUT, DELETE
class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response(
            {"detail": "This item deleted"}, status=status.HTTP_204_NO_CONTENT
        )

"""

''' This is an other way for Create and List view in Class with (GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin)
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)'''

''' Class Based View with with  (ListCreateAPIView, RetrieveUpdateDestroyAPIView)       
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class PostList(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    '''
    
''' Class Based View with (ViewSet)
from rest_framework import viewsets

class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def create(self, request):
        pass
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
'''

from rest_framework.viewsets import ModelViewSet

class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer