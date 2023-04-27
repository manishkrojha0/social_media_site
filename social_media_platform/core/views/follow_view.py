"""View file for follow."""

from rest_framework.views import APIView
from django.contrib.auth.models import User
from core.serializers.models_serializers import ProfileSerializer
from rest_framework.response import Response 
from rest_framework import status
from core.models.profiles import Profile

class FollowView(APIView):
    def post(self, request, id):
        try:
            user_to_follow = User.objects.get(id=id)
            profile = Profile.objects.get(user=user_to_follow)
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                user = request.user
                if user == user_to_follow:
                    return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
                print("==========================llll=================", user)
                if user.is_authenticated:
                    current_profile = Profile.objects.get(user=user)
                    current_profile.followings.add(profile.user)

                profile.followers.add(user.id)
                profile.save()
                return Response({'detail': f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)