from django.contrib.auth import get_user_model   ###현재 프로젝트에 활성화된 유저모델을 리턴해주기 위함. 장고의 권장사항. 장고는 모델을 직접참고하는걸 싫어한다.
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):  ##usercreationform 에 있는 meta 클래스를 상속 받는다.
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',) #이메일 필드가 추가됨. 옵션태그라서 회원가입할때 입력 안해도됨.

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)