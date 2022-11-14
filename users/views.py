from django.http import request
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import InfluencerSignupSerializer, BrandSignupSerializer, EmployeeSignupSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsBrandUser, IsInfluencerUser, IsEmployeeUser

class InfluencerSignupView(generics.GenericAPIView):
    serializer_class=InfluencerSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })


class BrandSignupView(generics.GenericAPIView):
    serializer_class=BrandSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })

class EmployeeSignupView(generics.GenericAPIView):
    serializer_class=EmployeeSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_client':user.is_client
        })

class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class BrandOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsBrandUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class InfluenecerOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsInfluencerUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class EmployeeOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsEmployeeUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user