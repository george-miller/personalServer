from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def index(request):
	return HttpResponse("hello");
