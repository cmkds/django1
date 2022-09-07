from django import forms ### 장고라이브러리에서 forms를 임포트함.
from .models import Article   ##############

# class ArticleForm(forms.Form):
#     NATION_A ='kr'
#     NATION_B ='ch'
#     NATION_C ='jp'
#     NATIONS_CHOICES = [
#         (NATION_A,'한국'),
#         (NATION_B,'중국'),
#         (NATION_C,'일본'),
#     ]

#     ##forms도 모델과 마찬가지로 forms안에 필드들이 설정되어있다.
#     title = forms.CharField(max_length=10)  ##max_length는 form에서는 필수 속성값이 아니다.
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
#     #nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article  #어떤 모델을 기반으로 할지
        fields = '__all__' #어떤 모델필드 중 어떤 것을 출력 할지
        #exclude = ('title',)  ##타이틀만 가져오기