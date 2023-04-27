from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.models.post import Post
from core.models.like import Like


class UnlikePostAPIView(APIView):
    """
    API view to unlike a post by the authenticated user.
    """
    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        like = Like.objects.filter(post=post, author=request.user).first()

        if like:
            like.delete()
            return Response({'detail': 'Post unliked successfully.'})
        else:
            return Response({'detail': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)
