from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    return render(request, 'count.html')
