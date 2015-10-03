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
		
		sameUserObjects = highScore.objects.filter(user=request.GET.get('user'))
		logger.error("Found entires with same user " + str(sameUserObjects))
		if sameUserObjects != []:
			for sameUser in sameUserObjects:
				if sameUser.score > request.GET.get('score'):
					return HttpResponse('This user has a high score saved')
			# If we didn't return, then this score is the
			# current highest for this user, so we must delete the redundant entries
			sameUserObjects.delete()

		hs = highScore()
		hs.score = request.GET.get('score')
		hs.user = request.GET.get('user')
		hs.save()
		return HttpResponse('Successfly saved high score')
	
	return HttpResponse('you are not a valid user')

def getLeaderboard(request):
	scores = [];
	scoreObjects = highScore.objects.all().order_by('-score')
	for scoreObj in scoreObjects:
		scores.append("score: " + str(scoreObj.score) +
			"  user: " + scoreObj.user + " <br/> ") 
	return HttpResponse(scores)
