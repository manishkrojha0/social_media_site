"""urls file for core app."""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views.custom_user_auth_views import CustomTokenObtainPairView
from .views.follow_view import FollowView
from core.views.user_profile_views import UserProfileView
from core.views.unfollow_view import UnfollowView
from core.views.user_info_views import UserInfoView
from core.views.post_create_view import PostCreateView
from core.views.post_details_view import PostDetailsView
from core.views.like_post_api_view import LikePostAPIView
from core.views.unlike_post_api_view import UnlikePostAPIView
from core.views.comment_create_view import CommentCreateAPIView
from core.views.all_posts_view import AllPostsAPIView
# from core.views.custom_user_auth_views import CustomTokenObtainPairView

urlpatterns = [
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/authenticate/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/follow/<int:id>/', FollowView.as_view(), name='follow'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
    path('api/unfollow/<int:id>/', UnfollowView.as_view(), name='unfollow'),
    path('api/user/', UserInfoView.as_view(), name='user_info'),
    path('api/posts/', PostCreateView.as_view(), name='post_create'),
    path('api/posts/<int:id>/', PostDetailsView.as_view(), name='post_details'),
    path('api/like/<int:id>/', LikePostAPIView.as_view(), name='like_create_view'),
    path('api/unlike/<int:id>/', UnlikePostAPIView.as_view(), name='unlike_post_view'),
    path('api/comment/<int:id>', CommentCreateAPIView.as_view(), name='create_comment'),
    path('api/all_posts/', AllPostsAPIView.as_view(), name='all_posts'),
]