from django import forms
from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        labels = {
            "title": "제목",
            "content": "내용",
            "image": "이미지",
        }


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "댓글을 입력해주세요."},
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "username",
            "content",
        ]
