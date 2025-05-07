from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Post

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

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.body, 'Test content')
        self.assertEqual(self.post.status, Post.Status.PUBLISHED)

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_get_absolute_url(self):
        expected_url = f'/blog/{self.post.publish.year}/{self.post.publish.month}/{self.post.publish.day}/{self.post.slug}/'
        self.assertEqual(self.post.get_absolute_url(), expected_url)

    def test_post_tags(self):
        self.post.tags.add('python', 'django')
        self.assertEqual(self.post.tags.count(), 2)
        self.assertEqual(set(self.post.tags.names()), {'python', 'django'})

    def test_post_status_choices(self):
        self.assertIn(Post.Status.DRAFT, Post.Status)
        self.assertIn(Post.Status.PUBLISHED, Post.Status)

    def test_post_ordering(self):
        # Create another post with a later publish date
        later_post = Post.objects.create(
            title='Later Post',
            slug='later-post',
            author=self.user,
            body='Later content',
            publish=timezone.now(),
            status=Post.Status.PUBLISHED
        )
        
        # Posts should be ordered by publish date in descending order
        posts = Post.objects.all()
        self.assertEqual(posts[0], later_post)
        self.assertEqual(posts[1], self.post)
