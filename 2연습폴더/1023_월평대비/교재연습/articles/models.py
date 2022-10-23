from django.db import models

# Create your models here.
class Article(models.Model):
    # # 
    #     title = 모델필드 100자 제한
    # content = 텍스트 필드 설정
    # created_at = 데이트타임 추가시간으로
    # updated_at = 수정시간으로

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):

    # article =외래키 설정
    # content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

