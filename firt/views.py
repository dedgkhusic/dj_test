from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    name = "susia"

    return render(request, 'home.html', {'name': name})
