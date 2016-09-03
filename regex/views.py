
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import highScore
import logging

def index(request):
    return render(request, 'regex.html')

def search(request):

