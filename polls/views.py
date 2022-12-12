from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from .models import Question, Choice

from .forms import QuestionForm
from django.contrib import messages

def index(request):
	latest_question=Question.objects.all()
	#output='<br>'.join([q.question_text for q in latest_question])
	#return HttpResponse(output)
	#return HttpResponse("<marquee> <h1>Welcome to My website</h1></marquee>")

	context={'latest_question_list':latest_question}
	
	return render(request,'polls/index.html',context)



def detail(request, question_id):

	question=get_object_or_404(Question,pk=question_id)

	context={'question':question}

	return render(request,'polls/detail.html',context)

def vote(request,question_id):
	question=get_object_or_404(Question,pk=question_id)

	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])

	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'question':question,
			'error_message':"You didn't select a choice",})
	else:
		selected_choice.votes += 1
		selected_choice.save()

	return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def results(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{'question':question})


def add_question(request):
	if request.method=='POST':
		question = QuestionForm(request.POST)
		if question.is_valid():
			question.save()
			messages.info(request,'Question Added successfully!')
			return HttpResponseRedirect(reverse("polls:index"))
		else:
			messages.info(request,'Invalid Data!')
			return HttpResponseRedirect(reverse("polls:add_question"))
	else:
		question=QuestionForm()
		return render(request,'polls/add_question.html',{'question':question})

# def add_choice(request,question_id):
# 	question=get_object_or_404(Question,pk=question_id)