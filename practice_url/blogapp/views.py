from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm
from django.contrib import auth
from django.contrib.auth.models import User


def home(request):
    # 블로그 글들을 모조리 띄우느 코드
    posts = Blog.objects.all()
    Blog.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts': posts})

# 블로그 글 작성 html을 보여주는 함수


def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수


def create(request):
    if (request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        # 모델 객체를 데이터베이스에 저장
        post.save()
    # 'home'으로 다시 돌아가라
    return redirect('home')

# django form을 이용해서 입력값을 받는 함수
# Get요청과 POST 요청 둘 다 처리가 가능한 함수
# Get 요청 - 입력값을 받을 수 있는 html을 갖다 줘야함
# POST 요청 - 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리


def formcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)

        if form.is_valid():  # form의 입력값이 유효한지 검사
            # 입력 내용을 저장하는 코드 작성
            post = Blog()
            # cleaned_data: 검사를 거친 깨끗한 데이터
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()  # model 객체인 post를 저장
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogForm()

    return render(request, 'form_create.html', {'form': form})


# django modelform을 이용해서 입력값을 받는 함수
def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():  # form의 입력값이 유효한지 검사
            form.save()  # form에서 입력한 값을 저장한다.
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form': form})


def detail(request, blog_id):
    # blog_id 현재 블로그 글을 DB로부 갖고와서 detail.html로 띄워주는 코드
    # pk 값을 이용해 특정 모델 객체 하나만 갖고오기
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'blog_detail': blog_detail, 'comment_form': comment_form})


def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)
