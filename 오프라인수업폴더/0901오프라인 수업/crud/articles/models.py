from django.db import models

# Create your models here.
class Article(models.Model):    #클래스는 Article models.의 Model을 상속 받는다.)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True) ##여기에 디폴트 값  설정 가능하다.
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title