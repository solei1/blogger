from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from collections import defaultdict
from .models import Article, Tag, Link
import markdown2

def index(request):
    return render(request, 'blog/home.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

class IndexView(ListView):
    template_name = "blog/archives.html"
    context_object_name = "article_list"
    model = Article

    def get_context_data(self, **kwargs):
        articles = defaultdict(list)
        sorted_article = list()
        # article_list = Article.objects.all().order_by('pub_date').reverse()
        article_list = Article.objects.all().order_by('-pub_date')
        year_list = sorted(list(set([article.pub_date.year for article in article_list])), reverse=True)
        for a in article_list:
            articles[a.pub_date.year].append(a)
        for single_year in year_list:
            sorted_article.append((single_year,articles[single_year]))
        kwargs['articles'] = sorted_article
        return super(IndexView, self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    template_name = "blog/article.html"
    context_object_name = "article"
    model = Article
    pk_url_kwarg = 'article_id'

    # def get_object(self):
    #     obj = super(ArticleDetailView, self).get_object()
    #     obj.body = markdown2.markdown(obj.body)
    #     return obj

class TagView(ListView):
    template_name = 'blog/tags.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'])
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all()
        kwargs['this_tag'] = Tag.objects.get(pk=self.kwargs['tag_id'])
        return super(TagView, self).get_context_data(**kwargs)

class LinkView(ListView):
    template_name = "blog/links.html"
    context_object_name = "links_list"
    model = Link

    def get_context_data(self, **kwargs):
        links = defaultdict(list)
        link_result = list()
        link_list = Link.objects.all()
        for link in link_list:
            links[link.category].append(link)
        for link_title, link_urls in links.items():
            link_result.append((link_title, link_urls))
        kwargs['links'] = link_result
        return super(LinkView, self).get_context_data(**kwargs)
