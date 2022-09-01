from django.shortcuts import render, redirect
from .models import Article ###모델즈 에서 아티클 가져옴

# Create your views here.
def index(request):
    #print(Article.objects.all())
    
    #articles =Article.objects.all()
    articles =Article.objects.order_by('-pk')  #생긴순서대로 역순 정렬하기.
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # print()
    # print(title,content)
    # print()
    
    ##리퀘스트 값을 DB에 저장하는 3가지 방법

    #1
    article= Article()
    article.title=title
    article.content=content
    article.save()

    #2
    # article = Article(title=title, content=content)
    # article.save()

    # #3
    # Article.objects.create(title=title, content=content)

    ######
    #return render(request,'articles/index.html')
    #return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article'  : article
    }
    return render(request, 'articles/detail.html',context)


def delete(request, pk):
    if request.method=="POST":

        article = Article.objects.get(pk=pk)
        article.delete()

    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html',context)



def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    article.save()

    return redirect('articles:detail', article.pk)
