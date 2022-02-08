from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from .feeds import LatestPostsFeed, LatestPostsFeed_es

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path("feed/en/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/es/rss", LatestPostsFeed_es(), name="post_feed_es"),
]
