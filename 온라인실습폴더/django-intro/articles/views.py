from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'articles/index.html')


def dtl(request):
    #name = 'jun'
    context = {
        'name': '가나다라마바사아자아차카타나',
        # 'age' : 20,
        'foods': ['apple', 'banana', 'pizza', 'chicken', 'hamburger']
    }
    return render(request, 'articles/dtl.html', context)


def greeting(request):
    return render(request, 'articles/greeting.html', {'name': 'Alice'})


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):

    # print(request.GET.get('search')) ####받은 GET값 확인하는 코드.
    value = request.GET.get('search')
    name = 'jun'  # 이랑 다를게 없는 코드.

    # 이 값을 context라는 딕셔너리에 담아서 전달한다.
    context = {
        'value': value,
        'name': name,
    }

    return render(request, 'articles/catch.html', context)


def hello(request, name):

    context = {
        'name': name,
    }
    return render(request, 'articles/catch.html', context)
