from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # mySite에서 polls.urls로 넘어 오면,,,,views로 넘어가고,,views안에 있는  함수 호출

    path('', views.index, name='index'),  # 8000/poll/아무것도 입력 안하면 -> index실행
    path('blog/', views.blog, name='blog'),  # 8000/polls/blog 하면 blog 함수 실행
    # 즉 path함수 맨 앞 인자는 url에서의 세부 경로-> 그 다음 인자는 그 세부 경로를 타고 들어왔을 때 뭘 실행할지, -> 그 다음 인자는 그 url의 이름!
    # url로부터 값을 넘겨 받아서 posting에 title을 전달!
    path('blog/<title>', views.posting, name="posting"),
    path('blog/new_post/', views.new_post, name="new_post"),
    path('blog/remove/<title>', views.remove_post, name="remove_post")
]
# return url patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 사진의 경로를 추가...
