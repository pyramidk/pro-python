from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Question, Choice
# Create your views here.

def index (request):
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    context = {
        'latest_question_list': latest_question_list,
    }
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail (request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_id = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) :
        return render (request, 'polls/detail.html', {
            'question': question,
            'error_message': "you didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
