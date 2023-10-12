from django.shortcuts import render
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404


def starting_page(request):
    return render("home.html")

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, request.data['username'])
    if not user.check_password(request.data['password']):
        return
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
    


def logout(request):
    try:
        token = Token.objects.get(user=user)
        user_token = token.key  
        token.delete()
    except Token.DoesNotExist:
        user_token = None
    
    logout(request)
