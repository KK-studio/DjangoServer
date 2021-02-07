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
def userSignup(request):
    try:
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
            myJson = json.loads(request.body)
            # print(str(myJson))
            # for i in myJson:
            #     print(str(i) +" " + str(myJson[i]))
            # print(myJson['id'])
            print("why")
            phone = myJson['phone']
            password = myJson['password']
            name = myJson['name']
            if not User.objects.filter(phone=phone).exists():
                newUser = User(phone=phone, password=password,name=name)
                newUser.save()
                responseData = {
                'state': True
                }

                return HttpResponse("ok")
            else:
                return HttpResponse("wrong")

    except:
        return HttpResponse("wrong2")


@csrf_exempt
def userLogin(request):
    try:
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
            myJson = json.loads(request.body)
            # print(str(myJson))
            # for i in myJson:
            #     print(str(i) +" " + str(myJson[i]))
            # print(myJson['id'])
            phone = myJson['phone']
            password = myJson['password']
            if User.objects.filter(phone=phone,password=password).exists():
                return HttpResponse("ok")
            else:
                return HttpResponse("wrong")

    except:
        return HttpResponse("wrong2")


@csrf_exempt
def docLogin(request):
    try:
        if request.method == 'POST':
            phone = myJson['phone']
            password = myJson['password']
            if Doctors.objects.filter(phone=phone,password=password).exists():
                return HttpResponse("ok")
            else:
                return HttpResponse("wrong")
    except:
        return HttpResponse("wrong2")

@csrf_exempt
def docSignup(request):
    try:
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
            myJson = json.loads(request.body)
            name = myJson['name']
            phone = myJson['phone']
            password = myJson['password']
            spec = myJson['spec']
            number = myJson['number']
            online_pay = myJson['online_pay']
            experience_years = myJson['experience_years']
            address = myJson['address']
            week_days = myJson['week_days']
            
            if not Doctors.objects.filter(phone=phone).exists():
                newUser = Doctors(phone=phone, password=password,name=name,spec=spec,number=number,online_pay=online_pay
                ,experience_years = experience_years,address=address,week_days=week_days)
                newUser.save()
                return HttpResponse("ok")
            else:
                return HttpResponse("wrong")

    except:
        return HttpResponse("wrong2")