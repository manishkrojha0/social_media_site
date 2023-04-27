from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.models_serializers import CommentSerializer
from core.models.comment import Comment
from core.models.post import Post

class CommentCreateAPIView(APIView):
    """API endpoint for adding a comment to a post"""

    serializer_class = CommentSerializer

    def post(self, request, id):
        """Add comment to post with given id"""

        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response({"error": f"Post with id={id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=request.data, context={"post_id": post.id, "author": request.user})

        if serializer.is_valid():
            comment = serializer.save(post=post, author=request.user)
            return Response({"comment_id": comment.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
