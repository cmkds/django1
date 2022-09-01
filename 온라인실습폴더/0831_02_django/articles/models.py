from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=10)  # 제목 10자 넘으면 저장 안시키겠다는 것
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title