from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) #해당 필드를 유효성 검사에서 제외 시키고 데이터 조회 시에는 출력 하도록함

class ArticleSerializer(serializers.ModelSerializer):
    
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  ##댓글 번호만 보여주기
    comment_set = CommentSerializer(many=True, read_only=True)               ## 댓글 내용 전부 보여주기.

    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
