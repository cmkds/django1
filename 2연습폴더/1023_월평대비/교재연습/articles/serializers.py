from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import Article, Comment



class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        field = ('id','title','content',)
    
    ## 아티클 모델 설정
    ## id, title, content 필드 설정


class CommentSerializer(serializers.ModelSerializer):

    # Comment 모델 설정
    ## 필드 전부 보여주기
    ## 리드 온리 필드 설정. 여기선 외래키인 article 필드 설정 해야함
    class Meta:
        model = Comment
        field = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):

    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only =True)
    comment_set = CommentSerializer(many=True, read_only = True)

    comment_count = serializers.IntegerField(source='comment_set.count', read_only = True)

    class Meta:
        model = Article
        field = '__all__'
    

    #  댓글 번호만 보여주기
    # 댓글 내용 전부 보여주기

    ## 댓글 수 보여주기.










