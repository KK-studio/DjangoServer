from django.shortcuts import render

from django.http import HttpResponse

from django.utils import timezone
from .models import Question,Doctors,User
from django.http import JsonResponse

import json

from django.views.decorators.csrf import csrf_exempt

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])

    if request.is_ajax():
        if request.method == 'GET':
            print('Raw Data: "%s"' % request.body)   

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
        b = Question(question_text='Beatles Blog', pub_date=timezone.now())
        b.save()
        return HttpResponse("None")
@csrf_exempt
def userLogin(request):
    # if request.is_ajax():
    if request.method == 'POST':
        print('Raw Data: "%s"' % request.body)
        myJson = json.loads(request.body)
        print(str(myJson))
        for i in myJson:
            print(str(i) +" " + str(myJson[i]))
        print(myJson['id'])
    return HttpResponse("ok")
