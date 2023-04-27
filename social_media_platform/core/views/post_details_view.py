from rest_framework import generics, permissions, status
from rest_framework.response import Response

from core.models.post import Post
from core.serializers.models_serializers import PostSerializer

class PostDetailsView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return None

    def get(self, request, id):
        post = self.get_object(id)
        if post:
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        user_id = request.user.id

        try:
            post = Post.objects.get(pk=post_id, author=user_id)
            self.check_object_permissions(request, post)
        except Post.DoesNotExist:
            return Response({'detail': 'Post does not exist or you do not have permission to delete it.'}, 
                            status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
