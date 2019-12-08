from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    return render(request, 'count.html', {'fulltext': fulltext})
