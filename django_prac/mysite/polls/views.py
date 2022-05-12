from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import Post


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    postlist = Post.objects.all()  # Post 객체(?)의 모든 정보를 postlist 변수에 담음
    # blog.html에게 알림. htlm파일 내부에 있는 postlist라는 것의 실제 내용물은 postlist란다~html파일이 response를 적절히 잘 처리하도록 전달?!
    return render(request, 'main/blog.html', {'postlist': postlist})
    # polls.urls에서 views로,,,!! 그리고 templates/main안에 있는 html파일
    # render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받음.
    # render를 하지 않으면 request에 대한 응답을 httpResponse로 전달할 수 있고, render를 쓰면,  render 함수의 optional한 3번째에 context로 표현해 httpresopnse를 반환할 수도 있음


def posting(request, title):
    # 게시글(Post) 중 title를 이용해 하나의 게시글(post)를 검색
    # postname이 title인 opbject만을 검색해서 post변수에다가 저장!!
    post = Post.objects.get(postname=title)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 돌려줌!
    # posting.html에게 post의 실인자는 post라는 것을 알림!! reponse 객체로, template과 share
    return render(request, 'main/posting.html', {'post': post})


def new_post(request):
    # new_post.html에서 form을 모두 입력하고, submit 버튼을 눌렀을 경우.
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(  # Post의 새로운 객체를 형성!사용자가 POST방식으로 전송한 정보를 바탕으로 새로운 Post 객체 형성

                # new_post method로 전달된 request 객체 안에 담긴 정보를 이용.
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/polls/blog/')  # 객체를 모두 만들었으므로,,, 게시판 목록으로 돌아가기!!
    # 아직 아무런 요청이 들어오지 않았다면, new_post.html 띄움..?
    return render(request, 'main/new_post.html')


def remove_post(request, title):
    post = Post.objects.get(postname=title)
    if request.method == 'POST':
        post.delete()
        return redirect('/polls/blog/')
    return render(request, 'main/remove.html', {'Post': post})

# new_post와 remove_post 구조는 잘 이해가 가지 않는다ㅏ.....submit에서 어떻게 이렇게 올 수 았는 것인지,...모르겠는데,,,action도 안넣었는데,,,?.,,,두 view가 같은 구조를 띄는 것을 보아...이렇게 작성하는 것인가.......
# 이해가 안간다....하다 보면 이해가 갈까...?
