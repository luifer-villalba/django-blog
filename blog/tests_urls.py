from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import post_list, post_detail

class TestUrls(SimpleTestCase):

    def test_post_list_url_is_resolved(self):
        url = reverse('blog:post_list')
        self.assertEquals(resolve(url).func, post_list)

    def test_post_detail_url_is_resolved(self):
        url = reverse('blog:post_detail', args=[1])
        self.assertEquals(resolve(url).func, post_detail)
