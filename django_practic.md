출처 : [https://wikidocs.net/91421](https://wikidocs.net/91421)

# Django

파이썬 웹 프레임워크

```
pip install django
```

## 장고 프로젝트 시작

```python
#danhan_venv 이름의 가상환경 만들기
python -m venv danhan_venv

#가상환경 실행
source danhan_venv/Scripts/activate

#장고 설치
pip install django

#프로젝트 만들기 - practice_django
django-admin startproject practice_django

#폴더 내부로 들어감
cd practice_django

#데이터 베이스 만들기
python manage.py migrate

#프로젝트 실행
python manage.py runserver

#작업 중지 -> 터미널로 빠져나오기
ctrl + c
```

## 첫 페이지 만들기

```python
#앱 시작 - 이름 main
python manage.py startapp main

#앱 등록
#practice_django/setting.py -> INSTALLED_APPS에 main 추가
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

#practice_django/main/templates/main/ 폴더에 임의의 index.html파일 생성
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    장고 첫페이지!
</body>
</html>

#생성한 html 파일 인코딩
#main/views.py 파일에 추가
from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

#view와 url 연결
#main/urls.py 파일 생성
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

#main 앱의 url과 practice_django 프로젝트의 url 연결
#practice_django/urls.py에 추가
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

#웹사이트 호스팅 (경로 주의)
python practice_django\\manage.py runserver
```

### render

html을 이용해 response를 생성하는 메소드

외부 urlConfig 하는 부분에서 에러가 나옴

```html
10. Including another URLconf 방식으로 하면 일어나는 일 - 사용자가
localhost:8000/polls에 접속하면 mysite/urls.py -> polls/urls.py -> view 순으로
연결이 됨. - localhost:8000/polls 은 mysite/urls.py 에서 처리하고 -
localhost:8000/polls/ ~~~~ 은 polls/urls.py에서 처리하게 되어 분리할 수 있음
```

[http://pythonstudy.xyz/python/article/311-URL-매핑](http://pythonstudy.xyz/python/article/311-URL-%EB%A7%A4%ED%95%91)

# 게시판 만들기

main/templates/main/blog.html

```html
<html>
  <head>
    <title>Blog List</title>
  </head>
  <body>
    <h1>게시판 페이지입니다</h1>
  </body>
</html>
```

main/view.py

```python
from django.shortcuts import render

# index.html 페이지를 부르는 index 함수
# 서버에 요청이 들어왔을 떄 index.html을 렌더링해서 보여준다
def index(request):
    return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    return render(request, 'main/blog.html')
```

main/urls.py

```python
from django.urls import path
from .views import *

app_name='main'

# views.py의 함수들과 url을 연결
urlpatterns=[
    path('',index),
		# 127.0.0.1:8000/blog일 경우 blog 함수 연결
    path('blog/',blog),
]
```

## Model

- post 게시글
- postname 제목
- contents 내용

main/models.py

```python
from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
```

model을 장고 db에 migrate

```python
# 웹 서버 종료 후
python manage.py makemigrations
python manage.py migrate
```

admin 권한 - 관리자 admin이 게시글 post에 접근할 권한 부여

main/admin.py

```python
from django.contrib import admin
# 게시글(Post) Model을 불러옵니다
from .models import Post

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post)
```

관리자 admin 계정 생성

```python
# superuser - 장고 프로젝트의 모든 app과 object를 관리하는 계정
# manage.py를 통해 superuser 계정이 생성
# username, email address, 강한 password 필요
python manage.py createsuperuser
```

```python
Username (leave blank to use 'danha'): admink
Email address:
Password:
Password (again):
```

### 게시글 작성

main/models.py

```python
from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname
```

### blog 목록 페이지에 게시판 띄우기

main/views.py

```python
from django.shortcuts import render
# View에 Model(Post 게시글) 가져오기
from .models import Post

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'main/blog.html', {'postlist': postlist})
```

Template에 Model 붙이기

== index.html에 post 게시글 붙이기

main/templates/main/blog.html

```html
<html>
  <head>
    <title>Blog List</title>
  </head>
  <body>
    <h1>게시판 페이지입니다</h1>
    <!-- 게시판(postlist)의 게시글(list)을 하나씩 보여줍니다 -->
    <!-- {%%} 내부엔 파이썬이 사용됩니다 -->
    <table>
      {% for list in postlist %}
      <ul>
        <li>{{list.postname}}</li>
        <li>{{list.contents}}</li>
      </ul>
      {% endfor %}
    </table>
  </body>
</html>
```

## 게시글 페이지 만들기

### `postdetails` 세부페이지 만들기

main/views.py

```python
from django.shortcuts import render
# View에 Model(Post 게시글) 가져오기
from .models import Post

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴
    return render(request, 'main/blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})
```

### 세부 페이지 들어가기

```python
from django.contrib import admin
from django.urls import path
# index는 대문, blog는 게시판
from main.views import index, blog, posting

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/', posting, name="posting"),
]
```

main/templates/main/posting.html

```html
<html>
  <head>
    <title>Posting!</title>
  </head>
  <body>
    <h1>게시글 개별 페이지입니다</h1>
    <p>{{post.postname}}</p>
    <p>{{post.contents}}</p>
  </body>
</html>
```

### 세부 페이지 연결

blog.html에서 제목을 클릭하면 posting 세부페이지로 넘어감

```html
<html>
  <head>
    <title>Blog List</title>
  </head>
  <body>
    <h1>게시판 페이지입니다</h1>
    <!-- 게시판(postlist)의 게시글(list)을 하나씩 보여줍니다 -->
    <!-- {와 %로 이루어진 구문 내부엔 파이썬이 사용됩니다 -->
    <table>
      {% for list in postlist %}
      <!-- 게시글 클릭시 세부페이지로 넘어갑니다-->
      <ul>
        <li><a href="./{{list.pk}}/">{{list.postname}}</a></li>
      </ul>
      {% endfor %}
    </table>
  </body>
</html>
```

posting 페이지에서 blog 페이지 링크

```html
<html>
  <head>
    <title>Posting!</title>
  </head>
  <body>
    <h1>게시글 개별 페이지입니다</h1>
    <p>{{post.postname}}</p>
    <p>{{post.contents}}</p>
    <a href="/blog/">목록</a>
  </body>
</html>
```

# 이미지 추가

blank=True 입력이 없어도 된다.

null=True db에서 null 값을 허용

\***\*`main/models.py`\*\***

```python
from django.db import models

class Post(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname
```

사진 처리 라이브러리 설치

```python
$ pip install pillow
$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python manage.py runserver
```

# 글쓰기 페이지

new_post.html 생성

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>글쓰기 페이지</title>
  </head>
  <body>
    <h1>글쓰기 페이지</h1>
    <form method="POST">
      {% csrf_token %} 제목<br />
      <input type="text" name="postname" /><br />
      내용<br />
      <textarea rows="10" cols="50" name="contents"></textarea><br />
      <input type="file" name="mainphoto" /><br />
      <input type="submit" value="글쓰기" />
    </form>
  </body>
</html>
```

<from> 내부의 정보를 한번에 서버로 전송

웹-서버 통신 방식

- GET 방식
  원하는 데이터를 서버에 요청해서 받아옴
- POST 방식
  정보를 서버에 전송하서 DB에 정보를 저장

crsf 사이트간 요청 위조

view 연결

main/views.py

```python
from django.shortcuts import redirect, render

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')
```

url 연결

main/urls.py

```python
from main.views import index, blog, posting, new_post

# 경로 추가
path('blog/new_post/', new_post),

```

글쓰기 버튼 추가

main/blog.html

```html
<button><a href="new_post/">글쓰기</a></button>
```

# 게시글 삭제

글 삭제 페이지 생성

templates/main/remove_post.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>글 삭제</title>
  </head>
  <body>
    <form method="POST">
      {% csrf_token %}
      <h3>{{ Post.postname }} - 삭제하기</h3>
      <button>삭제</button>
    </form>
  </body>
</html>
```

main/views.py

```python
def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})
```

urls 연결

main/urls.py

```python
from main.views import index, blog, posting, new_post, remove_post

path('blog/<int:pk>/remove/', remove_post),
```

posting.html

```python
<a href="/blog/{{post.pk}}/remove">삭제</a>v
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/66eed487-19f9-418b-be5f-bdd37722d801/Untitled.png)
