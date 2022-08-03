from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from questions.models import Question, Poll
from django.shortcuts import redirect
import random


def index(request):
    """

    """
    question_cont = Question.objects.count()
    question_num = random.randint(1, question_cont)
    question = Question.objects.get(id=question_num)
    return render(request, 'questions.html', {'question': question})


def save_poll(request):
    if request.method == 'POST':
        question_id = request.POST['question_id']
        try:
            poll = Poll.objects.get(question_id=question_id)
        except ObjectDoesNotExist:
            question = Question.objects.get(id=question_id)
            poll = Poll(question_id=question)
        poll.update_count(request.POST['ans'])
        poll.save()
        return redirect(f'/questions/poll_summary/{question_id}')


def summary_view(request, question_id):
    poll = Poll.objects.get(question_id=question_id)
    question = Question.objects.get(id=question_id)
    labels = ['Yes', 'No']
    data = [poll.yes_count, poll.no_count]
    return render(request, 'summary.html', {'labels': labels, 'data': data, 'question': question})
