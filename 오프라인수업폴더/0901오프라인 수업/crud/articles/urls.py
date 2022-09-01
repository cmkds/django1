from django.urls import path
from . import views   ##### views를 가져와서 쓰겠다.


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
        #<> 은 여기에 해당하는 값을 인자로 전달하겠다는 뜻.

    path('<int:pk>/delete/', views.delete, name='delete'),
    
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    

]


