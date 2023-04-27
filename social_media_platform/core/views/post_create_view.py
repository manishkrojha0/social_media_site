from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.post import Post
from core.serializers.models_serializers import PostSerializer

class PostCreateView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            post = serializer.save()
            return Response({
                'id': post.id,
                'title': post.title,
                'description': post.description,
                'created_at': post.created_at,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
