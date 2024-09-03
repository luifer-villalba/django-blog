from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            body='Test content',
            publish=timezone.now(),
            status=Post.Status.PUBLISHED
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/list.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:post_detail', args=[
            self.post.publish.year,
            self.post.publish.month,
            self.post.publish.day,
            self.post.slug
        ]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/detail.html')
