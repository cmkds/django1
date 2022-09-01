from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #request는 응답을 생성하는 데 사용되는 요청 객체
    #template_name 템플릿의 전체 이름 또는 템플릿 이름의 경로
    #context 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)
def greeting(request):
    foods = ['apple','banana','coconut',]
    info = {
        'name': 'Alice'
    }
    context = {
        'foods' : foods,
        'info': info,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['족발','햄버거','치킨','초밥',]
    pick = random.choice(foods)
    context = {
        'pick':pick,
        'foods':foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    
    # print(request)
    # print(type(request))
    # print(request.GET)
    # print(request.GET.get('message'))
    return render(request, 'catch.html')

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)