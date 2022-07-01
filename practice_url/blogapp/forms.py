from django import forms
from .models import Blog, Comment


class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog  # model을 기반으로
        fields = '__all__'  # Blog 객체의 모든 form(title, body, date)을 상속받기
        # fields = ['title', 'body']  # 특정 field만 상속받기


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
