from django.shortcuts import get_object_or_404, render,HttpResponse
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
    context ={
        'question':question
    }
    return render(request,'polls/detail.html',context)