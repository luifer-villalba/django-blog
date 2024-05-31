from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            body='Test content',
            publish=timezone.now(),
            status=Post.Status.PUBLISHED
        )

    def test_post_content(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.body, 'Test content')
