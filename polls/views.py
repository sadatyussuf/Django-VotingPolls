from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from .models import Question,Choice

# Create your views here.

def index(request):
    questions =Question.objects.order_by('-pub_date')
    context = {
        'questions':questions
    }
    return render(request,'polls/index.html',context)
    # return HttpResponse('We are live')

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    context ={
        'question':question
    }
    return render(request,'polls/detail.html',context)

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        context ={ 
            'question':question,
            'error_message': "You didn't select a choice."}
        return render(request,'polls/detail.html',context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results')


def results(request):
    questions = Question.objects.all()

    context ={ 'question':questions}
    return render(request,'polls/results.html',context)