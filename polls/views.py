from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
import logging
from .models import Question


def index(request):
	latestQuestionList = Question.objects.order_by('-pub_date')[:5]
	context = {'latestQuestionList': latestQuestionList}
	return render(request, 'polls/index.html', context)

def send(request):
	log = logging.getLogger(__name__)
	log.error("Oh please god")
	return HttpResponse("Hello?")

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
