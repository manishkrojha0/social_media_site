from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.models.like import Like
from core.models.post import Post
from core.serializers.models_serializers import LikeSerializer

class LikePostAPIView(APIView):
    
    def post(self, request, id):
         # Retrieve the post object
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response({"message": "Post Not found with this given id"}, status=status.HTTP_400_BAD_REQUES)

        # Create a like object
        like = Like(post=post, author=request.user)

        # Save the like object
        like.save()

        # Serialize the like object and return the response
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
