from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse

# Create your views here.

#Views for the index page
def index(request):
    #Querys the database and orders the object into date published
    questions =Question.objects.order_by('-pub_date')
    context = {
        'questions':questions
    }
    return render(request,'polls/index.html',context)

#Views for the detail page
def detail(request,question_id):
    #Querys the database
    question = get_object_or_404(Question,pk=question_id)
    context ={
        'question':question
    }
    return render(request,'polls/detail.html',context)


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        # Gets the choice submit by the user
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # checks to see if the user the submitted a choice
    except (KeyError,Choice.DoesNotExist):
        context ={ 
            'question':question,
            'error_message': "You didn't select a choice."}
        return render(request,'polls/detail.html',context)
    else:
        # Increamantes the votes based on the choice of the user
        selected_choice.votes += 1
        selected_choice.save()
        # return redirect('polls:results',pk=question_id)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    context ={ 'question':question}
    return render(request,'polls/results.html',context)


# Displays the JSON data of all the choices 
def resultsChart(request,question_id):
    # an empty list to store the choice_text and votes
    votedata = []
    # Querys the questions from the database
    question = get_object_or_404(Question,pk=question_id)
    # From the questions, choices are obtained because it is connected to the Question Model by a Foriegn Key
    votes = question.choice_set.all()    
    # iterate through the Choices
    for vote in votes:
        votedata.append({vote.choice_text:vote.votes})
    return JsonResponse(votedata,safe=False) 