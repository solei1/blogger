from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='blog_archives'),
    url(r'^article/(?P<article_id>\d+)', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^about$', views.about, name='about')
]