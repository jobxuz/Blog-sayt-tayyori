from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy

from .models import Article

def ArticleListView(request):
    blog = Article.objects.all()[::-1]
    return render(request,'main/article_list.html',{'blog_list':blog})



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'main/article_detail.html'


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ('title','summary','body','photo','categories',)
    template_name = 'main/article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'main/article_delete.html'
    success_url = reverse_lazy('articles_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Article
    template_name = 'main/article_new.html'
    fields = ('title','summary','body','photo','categories',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


def categoria_View(request):
    articl = Article.objects.filter(categories='Sport')[::-1]
    return render(request,'main/article_category.html',{'artcle': articl})


# class SportArticleDetailView(DetailView):
#     model = Article
#     template_name = 'main/sport_detail.html'


def SportArticleDetailView(request,pk):
    blog = Article.objects.get(pk=pk)
    return render(request,'main/sport_detail.html',{'blog':blog})


def uzbekiston_categoria_View(request):
    uzbek = Article.objects.filter(categories='Uzbekiston')[::-1]
    return render(request,'main/uzbek_category.html',{'uzbek': uzbek})


def UzbArticleDetailView(request,pk):
    blog = Article.objects.get(pk=pk)
    return render(request,'main/uzb_detail.html',{'blog':blog})