from django.shortcuts import render, redirect


def root(request):
    return render(request, "../templates/root.html")
