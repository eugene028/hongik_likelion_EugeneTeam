from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    # POST 요청은 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:  # 존재하는 회원이면
            auth.login(request, user)
            return redirect('home')
        else:  # 존재하지 않는 회원이면
            return render(request, 'login.html')
    # GET 요청은 login form 을 담고있는 login html 뜨움
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
