from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from core.models.post import Post
from core.models.like import Like

class PostDetailsViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post', description='This is a test post.', author=self.user)
        self.url = reverse('post_details', kwargs={'id': self.post.id})
    
    def test_retrieve_post_details(self):
        response = self.client.get(self.url)
        print(response.data, self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')
        self.assertEqual(response.data['description'], 'This is a test post.')
        self.assertEqual(response.data['author'], self.user.id)
    
    def test_delete_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
