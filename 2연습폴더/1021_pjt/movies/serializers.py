from rest_framework import serializers
from .models import Actor, Movie, Review



#############################
##출연 영화 제목 만 뽑기
class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ('title',)
        read_only_fields = ('title',)

### 출연 배우 이름 뽑기
class ActorNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('name',)
        read_only_fields = ('name',)

## 리뷰 목록 뽑기


##############################################

#전체 배우 목록 제공 
class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


## 단일 배우 정보 제공
class ActorSerializer(serializers.ModelSerializer):
    
    movies = MovieTitleSerializer(many=True, read_only=True) 

    class Meta:
        model = Actor
        fields = '__all__'

##############################################

##전체 리뷰 목록 제공

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title','content',)

##단일 리뷰 제공

class ReviewSerializer(serializers.ModelSerializer):
    
    movie = MovieTitleSerializer(read_only=True) 

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

##############################################


## 전체 영화 목록 제공
class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ('title','overview',)

## 단일 영화 목록 제공

class MovieSerializer(serializers.ModelSerializer):
    
    actors = ActorNameSerializer(many=True, read_only=True) 
    review_set = ReviewListSerializer(many=True, read_only=True) 

    # review = serializers.TextField(source='review_set.')

    class Meta:
        model = Movie
        fields = '__all__'


