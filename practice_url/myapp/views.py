from django.shortcuts import render


# 요청이 왔을 때 first.html을 찍어보내줘라(렌더링)
def first(request):
    return render(request, 'first.html')


def second(request):
    return render(request, 'second.html')
