from rest_framework import serializers
from core.models import profiles, post, like, comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    followers = UserSerializer(many=True)
    followings = UserSerializer(many=True)

    class Meta:
        model = profiles.Profile
        fields = ['user', 'followers', 'followings', 'bio']



class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = post.Post
        fields = ['id', 'title', 'description', 'created_at', 'author']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = comment.Comment
        fields = ['id', 'post', 'author', 'comment', 'created_at']

    def create(self, validated_data):
        post_data = validated_data.pop('post')
        author_data = validated_data.pop('author')

        from core.models.post import Post
        from core.models.profiles import Profile
        from core.models.comment import Comment
        
        print(type(post_data), type(author_data))

        post = Post.objects.get(id=post_data.id)
        author = Profile.objects.get(user=author_data.id)

        comment = Comment.objects.create(post=post, author=author, **validated_data)
        return comment


class LikeSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = like.Like
        fields = ['id', 'post', 'author']
