import operator

from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] = worddictionary[word] + 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(),
                         key=operator.itemgetter(1),
                         reverse=True)
    opts = {'sortedwords': sortedwords,
            'fulltext': fulltext,
            'count': len(wordlist)}
    
    return render(request, 'count.html', opts)
