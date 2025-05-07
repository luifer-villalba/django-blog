from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import post_list, post_detail, post_share

class TestUrls(SimpleTestCase):

    def test_post_list_url_is_resolved(self):
        url = reverse('blog:post_list')
        self.assertEqual(resolve(url).func, post_list)

    def test_post_detail_url_is_resolved(self):
        url = reverse('blog:post_detail', kwargs={
            'year': 2024,
            'month': 7,
            'day': 26,
            'post': 'sample-post'
        })
        self.assertEqual(resolve(url).func, post_detail)

    def test_post_share_url_is_resolved(self):
        url = reverse('blog:post_share', kwargs={'post_id': 1})
        self.assertEqual(resolve(url).func, post_share)

    def test_post_list_url_pattern(self):
        url = reverse('blog:post_list')
        self.assertEqual(url, '/blog/')

    def test_post_detail_url_pattern(self):
        url = reverse('blog:post_detail', kwargs={
            'year': 2024,
            'month': 7,
            'day': 26,
            'post': 'sample-post'
        })
        self.assertEqual(url, '/blog/2024/7/26/sample-post/')

    def test_post_share_url_pattern(self):
        url = reverse('blog:post_share', kwargs={'post_id': 1})
        self.assertEqual(url, '/blog/1/share/')
