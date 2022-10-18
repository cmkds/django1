from re import S
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from articles import serializers

from articles.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET','POST','PUT','DELETE'])
def article_list(request):
    if request.method =='GET':
        articles = get_list_or_404(Article)
        serializers = ArticleListSerializer(articles, many=True) #GET(모델변수, 목록일때 many=True)
        return Response(serializers.data) #GET은 리턴할때 serializers.data
    elif request.method =='POST':
        serializers = ArticleListSerializer(data=request.data) #POST는 data=request.data
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET','POST','PUT','DELETE'])
def article_detail(request, article_pk):
    if request.method =='GET':
        article = get_object_or_404(Article, pk=article_pk)
        serializers = ArticleSerializer(article) #GET(모델변수, 목록일때 many=True)
        return Response(serializers.data) #GET은 리턴할때 serializers.data
    elif request.method =='POST':
        serializers = ArticleSerializer(data=request.data) #POST는 data=request.data
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        article = get_object_or_404(Article, pk=article_pk)
        serializers = ArticleSerializer(article, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)


    elif request.method =='DELETE':
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#코멘트_list 리스트 겟으로 가져오기

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comment = get_list_or_404(Comment)
        serializers = CommentSerializer(comment, many = True)
        return Response(serializers.data)


##코멘트 detial GET, DELETE, PUT 하기
## 이건 아티클과 똑같다.
@api_view(['GET','PUT','DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404( Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializers = CommentSerializer(comment)
        return Response(serializers.data)

    elif request.method =='PUT':
        serializers = CommentSerializer(comment, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##코멘트 create POST로 만들기
@api_view(['POST'])
def comment_create(request, article_pk):
    if request.method =='POST':

        article = get_object_or_404(Article, pk=article_pk)

        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(article=article)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
