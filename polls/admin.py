from django.contrib import admin

from .models import Question, Choice, ipAlreadyVoted

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class ipInLine(admin.TabularInline):
	model = ipAlreadyVoted
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['question_text']}),
	('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInLine, ipInLine]
	list_display = ('question_text', 'pub_date')
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
