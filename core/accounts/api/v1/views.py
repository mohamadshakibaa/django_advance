from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegistraionSerializer, CustomAuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

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
        

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })