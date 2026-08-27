from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


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
    
    
"""
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
        # return Response({"detail":"Post dose not exist"}, status=status.HTTP_404_NOT_FOUND)/"""
        
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
        