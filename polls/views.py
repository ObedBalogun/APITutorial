from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question' #context_object_name is to override the default context variable "question_list"

    def get_queryset(self):
      #returns last 5 published questions with dates <= timezone.now()
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = ('polls/results.html')

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question,
                                                     'error_message':"You didn't select a choice"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
        #you should always return an HttpResponseRedirect after successfully dealing with POST data.