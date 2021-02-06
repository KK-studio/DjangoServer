from django.shortcuts import render

from django.http import HttpResponse


from .models import Question
from django.http import JsonResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_text):
    try:
        latest_question_list = Question.objects.filter(question_text__contains=question_text)
        responseData = {
        'id': latest_question_list[0].id,
        'date': latest_question_list[0].pub_date,
        'question' : latest_question_list[0].question_text
        }
        return JsonResponse(responseData)
    except:
        return HttpResponse("None")
