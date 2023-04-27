from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from core.models.profiles import Profile
from core.serializers.models_serializers import ProfileSerializer

class UserInfoView(APIView):
    def get(self, request):
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile)
            user_data = serializer.data
            data = {        
                    'username': user_data.get('user').get('username'),
                    'followers': len(user_data.get('followers')),
                    'followings': len(user_data.get('followings'))
                }
            return Response(data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'detail': "User profile not found."}, status=status.HTTP_400_BAD_REQUEST)
