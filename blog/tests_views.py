from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone
from django.core.exceptions import ValidationError

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
        # Create a draft post
        self.draft_post = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            body='Draft content',
            publish=timezone.now(),
            status=Post.Status.DRAFT
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/list.html')
        self.assertContains(response, self.post.title)
        self.assertNotContains(response, self.draft_post.title)

    def test_post_list_view_with_tag(self):
        # Add a tag to the post
        self.post.tags.add('python')
        response = self.client.get(reverse('blog:post_list_by_tag', args=['python']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertTemplateUsed(response, 'blog/post/list.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:post_detail', args=[
            self.post.publish.year,
            self.post.publish.month,
            self.post.publish.day,
            self.post.slug
        ]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/detail.html')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)

    def test_post_detail_view_invalid_slug(self):
        response = self.client.get(reverse('blog:post_detail', args=[
            self.post.publish.year,
            self.post.publish.month,
            self.post.publish.day,
            'invalid-slug'
        ]))
        self.assertEqual(response.status_code, 404)

    def test_post_detail_view_draft(self):
        response = self.client.get(reverse('blog:post_detail', args=[
            self.draft_post.publish.year,
            self.draft_post.publish.month,
            self.draft_post.publish.day,
            self.draft_post.slug
        ]))
        self.assertEqual(response.status_code, 404)

    def test_post_share_view(self):
        response = self.client.get(reverse('blog:post_share', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/share.html')

    def test_post_share_view_invalid_id(self):
        response = self.client.get(reverse('blog:post_share', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_post_share_view_post_method(self):
        response = self.client.post(reverse('blog:post_share', args=[self.post.id]), {
            'name': 'Test User',
            'email': 'test@example.com',
            'to': 'recipient@example.com',
            'comments': 'Test comment'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/share.html')
        self.assertContains(response, 'E-mail successfully sent')
