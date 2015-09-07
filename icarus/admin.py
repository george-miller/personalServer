from django.contrib import admin
from .models import highScore

class highScoreInLine(admin.TabularInline):
	model = highScore

class HighScoreAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['score', 'user' , 'creationDate']}),
	]
	list_display = ('score', 'user', 'creationDate')
	search_fields = ['user']

admin.site.register(highScore, HighScoreAdmin)
