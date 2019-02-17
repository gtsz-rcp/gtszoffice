import logging

from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import IntegrityError

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'])
    def auth(self, request):
        user = authenticate(
            username=request.data['username'], 
            password=request.data['password']
        )
        
        if user == None:
            return Response(False, status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key

        serializer = UserTokenSerializer(user)
        
        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
