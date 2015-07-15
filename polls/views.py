from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
import logging
from .models import Question, Choice, ipAlreadyVoted
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone

logger = logging.getLogger(__name__)
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
			pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
	
    def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
		logger.error(p.ipalreadyvoted_set.filter(ip=get_client_ip(request)).count())
		if p.ipalreadyvoted_set.filter(ip=get_client_ip(request)).count() == 0:
			selected_choice.votes += 1
			p.ipalreadyvoted_set.add(ipAlreadyVoted(ip=get_client_ip(request)))
			selected_choice.save()
			p.save()
			return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
		else:
			return render(request, 'polls/detail.html', {
				'question': p,
				'error_message': "You already voted"})

def newChoice(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	newChoice = Choice()
	newChoice.choice_text = request.POST['newChoice']
	question.choice_set.add(newChoice)
	question.save()
	return HttpResponseRedirect(reverse('polls:detail', kwargs=({'pk':question.pk})))
