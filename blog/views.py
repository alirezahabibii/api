from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article


# Create your views here.

class ArticleList(ListView):
    template_name = 'blog/article_list.html'

    def get_queryset(self):
        article: Article = Article.objects.filter(status=True)
        return article


class ArticleDetail(DetailView):
    def get_object(self, queryset=None):
        return get_object_or_404(Article.objects.filter(status=True), pk=self.kwargs.get('pk'))
