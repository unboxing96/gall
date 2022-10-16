from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    articles = Article.objects.all().order_by("-pk")
    page = request.GET.get("page", "1")
    paginator = Paginator(articles, 10)
    page_obj = paginator.get_page(page)
    context = {
        "article_list": page_obj,
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()

    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
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
    return render(request, "articles/create.html", context)


def search(request):

    dict = request.GET

    tong1 = dict["search"]
    tong2 = dict["keyword"]

    if dict["search"] == "user_name":
        article = Article.objects.filter(user_name__icontains=dict["keyword"]).order_by(
            "-pk"
        )
    elif dict["search"] == "title":
        article = Article.objects.filter(title__icontains=dict["keyword"]).order_by(
            "-pk"
        )
    elif dict["search"] == "content":
        article = Article.objects.filter(content__icontains=dict["keyword"]).order_by(
            "-pk"
        )

    context = {
        "tong1": tong1,
        "tong2": tong2,
        "article_list": article,
    }
    return render(request, "articles/search.html", context)
