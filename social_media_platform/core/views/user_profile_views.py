from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.models.profiles import Profile
from core.serializers.models_serializers import UserSerializer, ProfileSerializer


class UserProfileView(APIView):
    def get(self, request):
        """Endpoint to retrieve user's profile"""
        user = request.user
        try:
            user_profile = Profile.objects.get(user=user)
        except Exception:
            return Response({'message': "Profile is not registered."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Endpoint to create/update user's profile"""
        user = request.user
        print("===================", user)
        user_profile, created = Profile.objects.get_or_create(user=user)
        print(user_profile)
        serializer = ProfileSerializer(user_profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
