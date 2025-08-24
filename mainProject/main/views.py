from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страница")


def about(request):
    return render(request, "main/about.html")
