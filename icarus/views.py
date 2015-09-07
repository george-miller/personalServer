from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import highScore
import logging

logger = logging.getLogger(__name__)

def index(request):
	return HttpResponse("hello");

def recordHighScore(request):
	
	if request.GET.get('identity') == 'millercodesIcarus':
		if not(request.GET.get('score').isdecimal()) or not(isinstance(request.GET.get('user'), basestring)):
			return HttpResponse('Invalid Arguments')
		hs = highScore()
		hs.score = request.GET.get('score')
		hs.user = request.GET.get('user')
		hs.save()
		return HttpResponse('Successfly saved high score')
	
	return HttpResponse('recordHighSCore')

def getLeaderboard(request):
	return HttpResponse(highScore.objects.all())
