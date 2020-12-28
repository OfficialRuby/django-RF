from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins

from rest.models import User
from rest.serializer import UserSerializer


class userDetailsView(APIView):  # Using the APIView class
    permission_classes = [IsAuthenticated, ]
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        singlItem = users.first()
        # serialize = UserSerializer(users, many=True) #Serializing multiple items
        serialize = UserSerializer(singlItem) #Serializing a single Item

        return Response(serialize.data)

    def post(self, request, *args, **kwargs):
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)


class UserGenericView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset= User.objects.all()

    def get (self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post (self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)

class UserCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset= User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset= User.objects.all()

