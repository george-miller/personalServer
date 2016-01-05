
from django.shortcuts import render, get_object_or_404, render_to_response

def home(request):
	return render(request, 'index.html')
