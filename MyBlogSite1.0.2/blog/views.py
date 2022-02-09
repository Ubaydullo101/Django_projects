from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Article_View(ListView):
    model = Article
    template_name = 'index.html'

def article_detail(request,id):
    article=Article.objects.get(id=id)
    article.add_views
    return render(request=request,
           template_name='article_detail.html',
           context={
               'article':article
           })

class Article_Create_View(CreateView):
    model = Article
    template_name = 'new_article.html'
    fields = '__all__'

class Article_Update_View(UpdateView):
    model = Article
    template_name = 'article_update.html'
    fields = ['title','content','photo']

class Delet_Article(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('articles')
