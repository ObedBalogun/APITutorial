from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    questions= Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in questions])
    return HttpResponse(output)
def detail(request, question_id):
      return HttpResponse("This is question {}".format(question_id))
def results(request, question_id):
    return HttpResponse("The results of question %s are" % question_id)
def vote(request,question_id):
    return HttpResponse("You're voting on question %s" %question_id)