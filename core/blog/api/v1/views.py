from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view()
def postlist(request):
    return Response("ok")


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