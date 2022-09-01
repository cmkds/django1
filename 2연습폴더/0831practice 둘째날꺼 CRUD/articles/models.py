from django.db import models

# Create your models here.

class Article(models.Model):  ##django.db.modles 모듈의 Model 클래스를 상속받아 구성됨
    title = models.CharField(max_length=10)      #DB 필드의 이름 = DB필드의 데이터 타입
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title