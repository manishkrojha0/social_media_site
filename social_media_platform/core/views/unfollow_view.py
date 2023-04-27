from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from core.models.profiles import Profile


class UnfollowView(APIView):
    def post(self, request, id):
        # Get the user to unfollow
        print("fsfsdfsd")
        user_to_unfollow = get_object_or_404(User, id=id)

        print(user_to_unfollow)

        # Get the profile of the currently authenticated user
        current_profile = get_object_or_404(Profile, user=request.user)

        # Remove the user to unfollow from the current user's following list
        current_profile.followings.remove(user_to_unfollow.id)
        current_profile.save()

        # Remove the current user from the user to unfollow's followers list
        profile = get_object_or_404(Profile, user=user_to_unfollow)
        profile.followers.remove(request.user.id)
        print(profile.followers)
        profile.save()

        return Response({'detail': f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
