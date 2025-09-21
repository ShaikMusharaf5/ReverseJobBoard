from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.utils.timezone import now
from rest_framework.authtoken.models import Token
from .models import User, SearchAnalytics
from .serializers import UserSerializer


class CandidateSearchView(APIView):
    def get(self, request):
        role = request.GET.get('role', '').lower()
        min_exp = int(request.GET.get('min_experience', 0))
        min_rating = float(request.GET.get('min_rating', 0.0))

        if role:
            obj, created = SearchAnalytics.objects.get_or_create(role=role)
            obj.search_count += 1
            obj.last_searched = now()
            obj.save()

        return Response({"message": "Search processed"}, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')

        # Check for duplicate username or email and return error if found
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        # Use serializer to create user
        response = super().create(request, *args, **kwargs)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Login successful',
                'user_id': user.id,
                'role': user.role,
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
