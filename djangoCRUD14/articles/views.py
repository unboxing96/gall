from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by("-id")
    page = request.GET.get("page")  # 현재 몇 번째 페이지인지
    paginator = Paginator(articles, 10)  # (글 목록, 1페이지에 몇 개씩?)
    page_obj = paginator.get_page(page)  # 몇 번째 페이지 가져올지
    page_range = paginator.page_range

    context = {
        "articles": articles,
        "page_obj": page_obj,
        "page_range": page_range,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        "article": article,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
    }
    return render(request, "articles/update.html", context)


@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST, request.user)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect("articles:detail", article.pk)


@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect("articles:detail", article_pk)


def search(request):
    search_1 = request.GET.get("search_1")
    search_2 = request.GET.get("search_2")

    if search_1 == "title":
        search_articles = Article.objects.filter(title__icontains=search_2)
    elif search_1 == "content":
        search_articles = Article.objects.filter(content__icontains=search_2)
    elif search_1 == "username":
        search_articles = Article.objects.filter(
            user_id=get_user_model().objects.get(username=search_2)
        )

    page = request.GET.get("page")
    paginator = Paginator(search_articles, 10)
    page_obj = paginator.get_page(page)
    page_range = paginator.page_range

    context = {
        "search_1": search_1,
        "search_2": search_2,
        "search_articles": search_articles,
        "page_obj": page_obj,
        "page_range": page_range,
    }
    return render(request, "articles/search.html", context)


def like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect("articles:detail", article_pk)
