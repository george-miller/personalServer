from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from lib.python.regex import findall, compile

def index(request):
    return render(request, 'regex.html')

def search(request):
    graph = compile(request.POST['regex'])
    found = findall(request.POST['collection'], graph)
    return render(request, 'regex.html', {
        'results': found
    })
