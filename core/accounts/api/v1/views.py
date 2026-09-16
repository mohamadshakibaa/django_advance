from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import (
    RegistraionSerializer,
    CustomAuthTokenSerializer,
    MyTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ProfileApiViewSerializer,
)
from rest_framework.authtoken.views import APIView, ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from ...models import User, Profile
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from ..utils import CustomEmailThread
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed


class RegistrationApiView(generics.CreateAPIView):
    serializer_class = RegistraionSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistraionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation_email.tpl', {"token": token}, "admin@admin.com", to={email})
            CustomEmailThread(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
    # if not user.is_active:
    #     raise AuthenticationFailed("User is not active")
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})

class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ChangePasswordView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Password changed successfully."}, status=status.HTTP_200_OK
        )


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileApiViewSerializer
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
    

from django.core.mail import send_mail
class TestEmailSend(generics.GenericAPIView):

    def get(self, requset, *args, **kwargs):
        email_obj = EmailMessage('email/hello.tpl', {'user': "mohamad"}, "admin@admin.com",to=["mohamad@gmail.com"])
        CustomEmailThread(email_obj).start()
        return Response("email sent")
    

    def get_tokens_for_user(self, user):
        # if not user.is_active:
        #     raise AuthenticationFailed("User is not active")
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    

class ActivationApiView(APIView):
    def get(self, request, token, *args, **kwargs):
        # decode
        # object user
        # valid
        # or not valid
    
        return Response(token)
