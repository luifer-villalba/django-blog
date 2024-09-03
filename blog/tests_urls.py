from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import post_list, post_detail

class TestUrls(SimpleTestCase):

    def test_post_list_url_is_resolved(self):
        url = reverse('blog:post_list')
        self.assertEquals(resolve(url).func, post_list)

    def test_post_detail_url_is_resolved(self):
        url = reverse('blog:post_detail', kwargs={
            'year': 2024,
            'month': 7,
            'day': 26,
            'post': 'sample-post'
        })
        self.assertEquals(resolve(url).func, post_detail)
