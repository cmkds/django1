from django.urls import path
# 명시적 상대 경로
from . import views

# pages/urls.py
app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
