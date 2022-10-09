from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import GallForm, SelectForm
from .models import Gall

# Create your views here.
def index(request):
    galls = Gall.objects.all().order_by("-pk")
    paginator = Paginator(galls, 10)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "galls": page_obj,
    }
    return render(request, "galls/index.html", context)


def create(request):
    if request.method == "POST":
        form = GallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("galls:index")
    else:
        form = GallForm()

    context = {
        "form": form,
    }
    return render(request, "galls/create.html", context)


def detail(request, pk):
    gall = Gall.objects.get(pk=pk)
    context = {
        "gall": gall,
    }
    return render(request, "galls/detail.html", context)


def delete(request, pk):
    Gall.objects.get(pk=pk).delete()
    return redirect("galls:index")


def update(request, pk):
    gall = Gall.objects.get(pk=pk)
    if request.method == "POST":
        form = GallForm(request.POST, instance=gall)
        if form.is_valid():
            form.save()
            return redirect("galls:detail", gall.pk)
    else:
        form = GallForm(instance=gall)

    context = {
        "form": form,
    }
    return render(request, "galls/create.html", context)
