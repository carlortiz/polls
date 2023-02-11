from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    min_num = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ('date_created', 'question_text')
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
