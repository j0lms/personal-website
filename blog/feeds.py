from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
# from django.utils.feedgenerator import Atom1Feed
# from django.urls import reverse


class LatestPostsFeed(Feed):
    title = "Jorge Olmos"
    link = "https://jorgeolmos.pythonanywhere.com/blog/"
    description = "Posts EN"

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_enclosure_url(self, item):
        return 'https://jorgeolmos.pythonanywhere.com{}'.format(item.image.url)

    def item_enclosure_length(self, item):
        return '{}'.format(item.image.size)

    def item_enclosure_mime_type(self, item):
        return 'image/{}'.format(item.image.name.split('.')[-1])

    # Only needed if the model has no get_absolute_url method
    # def item_link(self, item):
    #     return reverse("post_detail", args=[item.slug])

class LatestPostsFeed_es(Feed):
    title = "Jorge Olmos"
    link = "https://jorgeolmos.pythonanywhere.com/blog/"
    description = "Posts ES"

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title_es

    def item_description(self, item):
        return truncatewords(item.content_es, 30)

    def item_enclosure_url(self, item):
        return 'https://jorgeolmos.pythonanywhere.com{}'.format(item.image.url)

    def item_enclosure_length(self, item):
        return '{}'.format(item.image.size)

    def item_enclosure_mime_type(self, item):
        return 'image/{}'.format(item.image.name.split('.')[-1])


    # Only needed if the model has no get_absolute_url method
    # def item_link(self, item):
    #     return reverse("post_detail", args=[item.slug])

# class MyFeed(Feed):
#    feed_type = Atom1Feed