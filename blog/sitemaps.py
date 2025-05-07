from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse
from taggit.models import Tag


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj):
        return obj.updated


class TagSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        # Only include tags that are actually used in published posts
        return Tag.objects.filter(post__status=Post.Status.PUBLISHED).distinct()

    def location(self, obj):
        return reverse('blog:post_list_by_tag', args=[obj.slug])

    def lastmod(self, obj):
        # Get the most recent post for this tag
        return Post.published.filter(tags=obj).latest('updated').updated