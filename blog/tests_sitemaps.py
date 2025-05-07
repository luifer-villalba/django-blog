from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .models import Post
from .sitemaps import PostSitemap, TagSitemap
from taggit.models import Tag


class SitemapTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Create some tags
        self.tag1 = Tag.objects.create(name='python', slug='python')
        self.tag2 = Tag.objects.create(name='django', slug='django')
        
        # Create published posts
        self.published_post1 = Post.objects.create(
            title='Published Post 1',
            slug='published-post-1',
            author=self.user,
            body='Test content 1',
            publish=timezone.now(),
            status=Post.Status.PUBLISHED
        )
        self.published_post1.tags.add(self.tag1, self.tag2)
        
        self.published_post2 = Post.objects.create(
            title='Published Post 2',
            slug='published-post-2',
            author=self.user,
            body='Test content 2',
            publish=timezone.now(),
            status=Post.Status.PUBLISHED
        )
        self.published_post2.tags.add(self.tag1)
        
        # Create a draft post
        self.draft_post = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            body='Draft content',
            publish=timezone.now(),
            status=Post.Status.DRAFT
        )
        self.draft_post.tags.add(self.tag2)

    def test_post_sitemap_items(self):
        """Test that PostSitemap only includes published posts"""
        sitemap = PostSitemap()
        items = sitemap.items()
        
        self.assertEqual(items.count(), 2)
        self.assertIn(self.published_post1, items)
        self.assertIn(self.published_post2, items)
        self.assertNotIn(self.draft_post, items)

    def test_post_sitemap_lastmod(self):
        """Test that PostSitemap returns correct lastmod"""
        sitemap = PostSitemap()
        lastmod = sitemap.lastmod(self.published_post1)
        self.assertEqual(lastmod, self.published_post1.updated)

    def test_post_sitemap_priority(self):
        """Test that PostSitemap has correct priority"""
        sitemap = PostSitemap()
        self.assertEqual(sitemap.priority, 0.9)

    def test_post_sitemap_changefreq(self):
        """Test that PostSitemap has correct changefreq"""
        sitemap = PostSitemap()
        self.assertEqual(sitemap.changefreq, 'weekly')

    def test_tag_sitemap_items(self):
        """Test that TagSitemap only includes tags from published posts"""
        sitemap = TagSitemap()
        items = sitemap.items()
        
        self.assertEqual(items.count(), 2)
        self.assertIn(self.tag1, items)
        self.assertIn(self.tag2, items)

    def test_tag_sitemap_location(self):
        """Test that TagSitemap generates correct URLs"""
        sitemap = TagSitemap()
        location = sitemap.location(self.tag1)
        expected_url = reverse('blog:post_list_by_tag', args=[self.tag1.slug])
        self.assertEqual(location, expected_url)

    def test_tag_sitemap_lastmod(self):
        """Test that TagSitemap returns correct lastmod"""
        sitemap = TagSitemap()
        lastmod = sitemap.lastmod(self.tag1)
        # Should be the most recent post's update time
        expected_lastmod = max(
            self.published_post1.updated,
            self.published_post2.updated
        )
        self.assertEqual(lastmod, expected_lastmod)

    def test_tag_sitemap_priority(self):
        """Test that TagSitemap has correct priority"""
        sitemap = TagSitemap()
        self.assertEqual(sitemap.priority, 0.8)

    def test_tag_sitemap_changefreq(self):
        """Test that TagSitemap has correct changefreq"""
        sitemap = TagSitemap()
        self.assertEqual(sitemap.changefreq, 'daily') 