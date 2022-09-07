import re
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm   ####모든 앱에 있는 forms 파이썬 파일에서 ArticleForm 클래스를 사용할 수 있도록 가져온다.


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


def create(request):

    ########### Handling HTTP requests
    if request.method == 'POST':
        #create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:
        # new
        form = ArticleForm()
    
    ##상황에 따라 2가지 form을 수행하는 위치가 됨.
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)













    # form = ArticleForm(request.POST)
    # if form.is_valid():
    #     article = form.save()
    #     return redirect('articles:detail', article.pk)
    # print(f'에러: {form.errors}')
    # #return redirect('articles:new')
    # #isvalid를 통과하지 못했을 때는 리다이렉트가 아니고 오류메세지가 포함된 페이지를 줘야한다.
    
    # ##여기로 내려온 form은 실패한 form 이다.
    # context = {
    #     'form': form,
    # }

    # return render(request, 'articles/new.html', context)
    
    # # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # # DB에 저장
    # # 1
    # # article = Article()
    # # article.title = title
    # # article.content = content
    # # article.save()

    # # 2
    # article = Article(title=title, content=content)
    # article.save()

    # # 3
    # # Article.objects.create(title=title, content=content)

    # # return render(request, 'articles/index.html')
    # # return redirect('/articles/')
    # # return redirect('articles:index')
    # return redirect('articles:detail', article.pk)


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()    
        return redirect('articles:index')
    return redirect('articles:index', article.pk)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article) # form에 기존데이터를 변수로 넣어줌.
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):

    ###################
    article = Article.objects.get(pk=pk)
    ##########
    if request.method == 'POST':
        #####DB
        form = ArticleForm(request.POST, instance=article)   ##instance= article 이 코드로 생성인지 수정인지 판단함.
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        ####수정페이지
        form = ArticleForm(instance=article) # form에 기존데이터를 변수로 넣어줌.
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)







    # article = Article.objects.get(pk=pk)
    
    # form = ArticleForm(request.POST, instance=article)   ##instance= article 이 코드로 생성인지 수정인지 판단함.
    # if form.is_valid():
    #     form.save()
    #     return redirect('articles:detail', article.pk)
    # context = {
    #     'form' : form,
    #     #'article' : article,
    # }
    # return render(request, 'articles/edit.html', context)


    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)