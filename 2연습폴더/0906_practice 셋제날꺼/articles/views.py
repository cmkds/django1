from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)  ##유효성 검사를 통과하면 데이터 저장후, 상세페이지로 리다이렉트
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회

    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':  ##POST 요청에 대해서만 삭제가 가능하도록 수정.
        article.delete()
        return redirect('articles:index')
    return redirect('articles: detail', article.pk)

@require_http_methods(['GET','POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
       form = ArticleForm(instance=article) 
    context = {
        'form' : form,  
        'article' : article,
    }
    return render(request, 'articles/update.html', context)
    

