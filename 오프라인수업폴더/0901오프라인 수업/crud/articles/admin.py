from django.contrib import admin
from .models import Article  ##모델의 아티클 가져오기

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_at','updated_at')

admin.site.register(Article, ArticleAdmin) #어드민 사이트에 내 모델을 등록할거야