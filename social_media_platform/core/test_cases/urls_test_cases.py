from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from core.models.post import Post
from core.models.comment import Comment
from core.models.profiles import Profile

class UrlsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_token_verify_url(self):
        url = reverse('token_verify')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_token_obtain_pair_url(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_follow_url(self):
        user2 = User.objects.create_user(
            username='testuser2', email='testuser2@test.com', password='testpass')
        # create file of current user.
        Profile.objects.create(user=self.user, bio="test")
        url = reverse('follow', args=[user2.pk])
        self.client.force_authenticate(user=self.user)
        # create profile of user to be followed.
        Profile.objects.create(user=user2, bio="test")
        response = self.client.post(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_profile_url(self):
        url = reverse('profile')
        Profile.objects.create(user=self.user, bio="test")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unfollow_url(self):
        user2 = User.objects.create_user(
            username='testuser2', email='testuser2@test.com', password='testpass')
        self.client.force_authenticate(user=self.user)
        # create file of current user.
        Profile.objects.create(user=self.user, bio="test")
        # create profile of user to be unfollowed.
        Profile.objects.create(user=user2, bio="test")
        url = reverse('unfollow', args=[user2.pk])
        response = self.client.post(url)
        print(response.data, "responseeeeeeeeeeee")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_info_url(self):
        url = reverse('user_info')
        Profile.objects.create(user=self.user, bio="test")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_url(self):
        url = reverse('post_create')
        data = {'title': 'test post', 'description': 'test content'}
        Profile.objects.create(user=self.user, bio="test")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_details_url(self):
        post = Post.objects.create(title='test post', description='test content', author=self.user)
        url = reverse('post_details', args=[post.pk])
        Profile.objects.create(user=self.user, bio="test")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_create_view_url(self):
        post = Post.objects.create(title='test post', description='test content', author=self.user)
        url = reverse('like_create_view', args=[post.pk])
        Profile.objects.create(user=self.user, bio="test")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return post.id

    def test_unlike_post_view_url(self):
        # post = Post.objects.create(title='test post', description='test content', author=self.user)
        post_id = self.test_like_create_view_url()
        url = reverse('unlike_post_view', args=[post_id])
        response = self.client.post(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_comment_url(self):
        post = Post.objects.create(title='test post', description='test content', author=self.user)
        url = reverse('create_comment', args=[post.pk])
        Profile.objects.create(user=self.user, bio="test")
        print(url)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
