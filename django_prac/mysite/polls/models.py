from django.db import models

# Create your models here.

# model은 일종의 '틀' 같은 것. post 클래스에는 내용과 제목을 담는 두가지 영역이 존재
# 장고의 db가 테이블을 저장하기 위해서,,model에 변경사항이 있을 때 마다 python manage.py makemigrations/ python manage.py migrate 해줘야 함!


class Post(models.Model):

    mainphoto = models.ImageField(blank=True, null=True)
    # CharField()함수는 길이가 정해져 있는 text를 저장하기 위해서 사용
    postname = models.CharField(max_length=50)
    contents = models.TextField()  # TextField는 길이가 정해져 있지 않은 text를 저장하기 위해서 사용

    def __str__(self):
        return self.postname
    # 게시글의 제목을 postname으로 표현하기 위한 함수입니다.``
