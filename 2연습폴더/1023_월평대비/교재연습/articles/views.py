from logging import raiseExceptions
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from articles import serializers

from articles.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment



# GET, POST  아티클 리스트 전부
## 시리얼라이저 구현
## JSON 형태로 반환

@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(data = serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

####
## 개별 GET, POST ,PUT DELETE 구현


@api_view(['GET','POST','PUT','DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
## 코멘트 list 겟으로 가져오기
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    if request.method == 'GET':
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


## 코멘트 detail, GET , DELETE, PUT 하기

@api_view(['GET','POST','PUT','DELETE'])
def comment_detail(request, comment_pk):

    comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method =='GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method =='PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method =='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## 코멘트 create POST 만들기
def comment_create(request, article_pk):












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
