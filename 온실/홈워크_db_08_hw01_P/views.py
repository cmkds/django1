# 홈워크_db_08_hw01_P-2.py
# views.py

from .serializers import MusicListSerializer, __(a)__ MusicListSerializer
from rest_framework.response import __(d)__ Response


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = __(a)__(musics, __(c)__) MusicListSerializer, many=True
    return __(d)__(serializer.__(e)__) Response,    data