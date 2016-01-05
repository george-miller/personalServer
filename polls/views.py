from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
import logging
from .models import Question, Choice, ipAlreadyVoted
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)
def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def index(request):
	return render(request, 'polls/index.html', {'latest_question_list': Question.objects.all()})

def detail(request, question_id):
	return render(request, 'polls/detail.html', {'question': Question.objects.get(pk=question_id)})


def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	logger.error(p);
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return HttpResponse("You didn't select a choice.")
	else:
		logger.error(selected_choice);
	if p.ipalreadyvoted_set.filter(ip=get_client_ip(request)).count() == 0:
		selected_choice.votes += 1
		ip = ipAlreadyVoted(ip=get_client_ip(request), question_id=p.id)
		ip.save()
		p.ipalreadyvoted_set.add(ip)
		selected_choice.save()
		p.save()
		return HttpResponseRedirect(reverse('polls:detail', args=(p.id,)))
	else:
		return HttpResponse("You already voted")

def addChoice(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	for choice in question.choice_set.all():
		if choice.choice_text == request.POST['newChoice']:
			return HttpResponse("Choice already exists")
			
	newChoice = Choice(question_id=question.id)
	newChoice.choice_text = request.POST['newChoice']
	newChoice.save()
	question.choice_set.add(newChoice)
	question.save()
	return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))


def addQuestion(request):
	for question in Question.objects.all():
		if question.question_text == request.POST.get('newQuestion', False):
			return HttpResponse("Question already exists");
	
	newQuestion = Question(question_text=request.POST.get('newQuestion', False), pub_date=timezone.now())
	newQuestion.save()
	return HttpResponseRedirect(reverse('polls:index'))
