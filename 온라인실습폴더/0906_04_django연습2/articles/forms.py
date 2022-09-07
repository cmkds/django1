from socket import fromshare
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder' : 'Enter the title',
                'maxlength': 10,
            }
        ),

    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 입력해 주세요',
                'rows': 5,
                'cols' : 50,
            }
        ),
        error_messages={
            'required' : 'Please enter your content'
        }
    )

    class Meta:
        model = Article   ###이건 호출하지 않고 이름만 작성하는 방식이다.
                          ###호출하지 않고 자체를 그대로 전달하여, 다른곳에서 "필요한 시점에" 호출한다.
                          ### Article 이라는 클래스를 호출하지 않고(== modle 인스턴스로 만들지 않고)
                          ### 작성하는 이유는 ArticleForm이 해당 클래스를 필요한 시점에 사용하기 위함.
                          ### 더불어 이 경우에는 인스턴스가 필요한 것이 아닌, 실제 Article 모델의 참조 값을 통해
                          ### 해당 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유도 있음
        fields = '__all__'
        #exclude = ('title',)


# class ArticleForm(forms.Form):

#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)

#     ##다른 위젯
#     # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect())
