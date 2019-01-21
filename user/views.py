from django.http import HttpResponse
from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):

    @action(detail=False, methods=['POST'])
    def auth(self, request):
        user = authenticate(username=request.username, password=request.passowrd)
        if user == None:
            return Response(False, status.HTTP_401_UNAUTHORIZED)
        token = Token.objects.create(user=user)
        return Response(token, status.HTTP_200_OK)
