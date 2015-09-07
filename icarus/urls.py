from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^recordHighScore$', views.recordHighScore, name = 'recordHighScore'),
	url(r'^getLeaderboard$', views.getLeaderboard, name='getLeaderboard')
]
