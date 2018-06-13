from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext'] #fulltext object yysgej bn
    # fulltext form iin GET medeelliig fulltext var-t onooj bn.

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext' : fulltext,  'count': len(wordlist), 'sortedwords': sortedwords })

def about(request):
    return render(request, 'about.html')
