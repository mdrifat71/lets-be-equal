from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import UserSerializer
class SignUpUser(APIView):

    def post(self, request):
        data = request.data
        # print(data)
        serializer = UserSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            'status' : 'success',
            'payload' : serializer.data
        }
        return Response(res_data, status = status.HTTP_201_CREATED)

    
    # only for dev
    def get(self,request):
        data = User.objects.all()
        serializer = UserSerializer(data, many = True)

        res_data = {
            'status' : 'success',
            'payload' : serializer.data
        }

        return Response(res_data, status = status.HTTP_200_OK)


