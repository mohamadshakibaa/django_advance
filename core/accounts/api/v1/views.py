from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegistraionSerializer

class RegistrationApiView(generics.CreateAPIView):
    serializer_class = RegistraionSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistraionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "email": serializer.validated_data("email")
            }
            return Response(data, status=status.HTTP_201_CREATED)