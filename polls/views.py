from django.shortcuts import render, redirect
from django.utils import timezone
from . import models


def display_questions(request):
    question_list = models.Question.objects.filter(date_created__lte=timezone.now())
    context = { 'question_list': question_list } 
    return render(request, 'polls/questions.html', context)


def display_choices(request, question_id):
    question = models.Question.objects.get(id=question_id)
    context = { 'question': question }
    return render(request, 'polls/choices.html', context)


def register_vote(request, question_id):
    question = models.Question.objects.get(id=question_id)
    try:
        choice = question.choice_set.get(id=request.POST['choice'])
    except(KeyError, models.Choice.DoesNotExist):
        error_message = "Error: You must pick a choice."
        context = { 'question': question, 'error_message': error_message }
        return render(request, 'polls/choices.html', context)
    else:
        choice.votes += 1
        choice.save()
        return redirect('results', question_id)


def display_results(request, question_id):
    question = models.Question.objects.get(id=question_id)
    context = { 'question': question }
    return render(request, 'polls/results.html', context)


# need a voting function 

