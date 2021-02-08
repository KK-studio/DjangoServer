from django.shortcuts import render

from django.http import HttpResponse

from django.utils import timezone
from .models import Question,Doctors,User,Comments
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
            
            if not Doctors.objects.filter(phone=phone).exists():
                newUser = Doctors(phone=phone, password=password,name=name)
                newUser.save()
                return HttpResponse("ok")
            else:
                return HttpResponse("wrong")

    except:
        return HttpResponse("wrong2")


@csrf_exempt
def editDoc(request):
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
            week_days = str(myJson['week_days'])
            
            if  Doctors.objects.filter(phone=phone).exists():
                newUser = Doctors(phone=phone, password=password,name=name,spec=spec,number=number,online_pay=online_pay
                ,experience_years = experience_years,address=address,week_days=week_days)
                newUser.save()
                return HttpResponse("ok")
            
        if request.method == 'GET':
            print('GET Raw Data: "%s"' % request.body)
            myJson = json.loads(request.body)
            phone = myJson['phone']
            password = myJson['password']

        
            if Doctors.objects.filter(phone=phone,password=password).exists():
                data = Doctors.objects.filter(phone=phone,password=password)
                myJson = {
                'name' : data[0].name,
                'phone' : data[0].phone,
                'password' : data[0].password,
                'spec' : data[0].spec,
                'number' : data[0].number,
                'online_pay' : data[0].online_pay,
                'experience_years' : data[0].experience_years,
                'address' : data[0].address,
                'week_days' : data[0].week_days,
                'score' : data[i].total_scores_sum / data[i].scores_count
                }
                return JsonResponse(myJson)
            else:
                return HttpResponse("wrong")
        return HttpResponse("none")

    except:
        return HttpResponse("wrong2")






@csrf_exempt
def SearchDoc(request,text):
    try:
        if text.startswith("name="):
            print("shit")
            text = text.replace("name=","")
            data = Doctors.objects.filter(name__contains=text)
            myList = []
            print("why")
            for i in range(len(data)):
                myJson = {
                'name' : data[i].name,
                'phone' : data[i].phone,
                'password' : data[i].password,
                'spec' : data[i].spec,
                'number' : data[i].number,
                'online_pay' : data[i].online_pay,
                'experience_years' : data[i].experience_years,
                'address' : data[i].address,
                'week_days' : data[i].week_days,
                'score' : data[i].total_scores_sum / data[i].scores_count
                }
                myList.append(myJson)
                print("hi")
            result = {'result' : myList} 
            return JsonResponse(result)

        elif text.startswith("spec="):
            print("shit")
            text = text.replace("spec=","")
            data = Doctors.objects.filter(spec__contains=text)
            myList = []
            print("why")
            for i in range(len(data)):
                myJson = {
                'name' : data[i].name,
                'phone' : data[i].phone,
                'password' : data[i].password,
                'spec' : data[i].spec,
                'number' : data[i].number,
                'online_pay' : data[i].online_pay,
                'experience_years' : data[i].experience_years,
                'address' : data[i].address,
                'week_days' : data[i].week_days,
                'last_Comment' : data[i].last_Comment,
                'score' : data[i].total_scores_sum / data[i].scores_count,
                'scores_count' : data[i].scores_count,
                }
                myList.append(myJson)
                print("hi")
            result = {'result' : myList} 
            return JsonResponse(result)
        
    except:
        return HttpResponse("None")





@csrf_exempt
def getDoc(request):
    try:
        print('GET Raw Data: "%s"' % request.body)
        myJson = json.loads(request.body)
        phone = myJson['phone']
        if Doctors.objects.filter(phone=phone).exists():
            data = Doctors.objects.filter(phone=phone)
            comments = []
            data2 = Comments.objects.filter(doc_phone=phone)
            for i in range(len(data2)):
                newJson = {
                    'name':data2[i].name,
                    'comment':data2[i].comment
                }
                comments.append(newJson)
            myJson = {
            'name' : data[0].name,
            'phone' : data[0].phone,
            'password' : data[0].password,
            'spec' : data[0].spec,
            'number' : data[0].number,
            'online_pay' : data[0].online_pay,
            'experience_years' : data[0].experience_years,
            'address' : data[0].address,
            'week_days' : data[0].week_days,
            'score' : data[0].total_scores_sum / data[0].scores_count,
            'comments' : comments
            }
            return JsonResponse(myJson)

    except:
        return HttpResponse("wrong2")



@csrf_exempt
def addComment(request):
    try:
        print('GET Raw Data: "%s"' % request.body)
        myJson = json.loads(request.body)
        phone = myJson['phone']
        name = myJson['name']
        comment = myJson['comment']
        if Doctors.objects.filter(phone=phone).exists():
            Doctors.objects.filter(phone=phone)[0].last_Comment = comment
            newCooment = Comments(doc_phone=phone,name = name,comment=comment)
            newCooment.save()
            return HttpResponse("ok")

    except:
        return HttpResponse("wrong2")

@csrf_exempt
def addScore(request):
    try:
        print('GET Raw Data: "%s"' % request.body)
        myJson = json.loads(request.body)
        phone = myJson['phone']
        score = myJson['score']
        if Doctors.objects.filter(phone=phone).exists():
            Doctors.objects.filter(phone=phone)[0].scores_count += 1
            Doctors.objects.filter(phone=phone)[0].total_scores_sum += score
            newScore.save()
            return HttpResponse("ok")

    except:
        return HttpResponse("wrong2")



@csrf_exempt
def editUser(request):
    try:
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
            myJson = json.loads(request.body)
            name = myJson['name']
            phone = myJson['phone']
            password = myJson['password']
        
            if  User.objects.filter(phone=phone).exists():
                newUser = User(phone=phone, password=password,name=name)
                newUser.save()
                return HttpResponse("ok")

        if request.method == 'GET':
            print('GET Raw Data: "%s"' % request.body)
            myJson = json.loads(request.body)
            phone = myJson['phone']
            password = myJson['password']

        
            if User.objects.filter(phone=phone,password=password).exists():
                data = User.objects.filter(phone=phone,password=password)
                myJson = {
                'name' : data[0].name,
                'phone' : data[0].phone,
                'password' : data[0].password,
                }
                return JsonResponse(myJson)
        return HttpResponse("oops!")

    except:
        return HttpResponse("wrong2")



@csrf_exempt
def getUser(request,text):
    try:
        if request.method == 'GET':
            print('GET Raw Data: "%s"' % request.body)
            # myJson = json.loads(request.body)
            phone = text

        
            if User.objects.filter(phone=phone).exists():
                data = User.objects.filter(phone=phone)
                myJson = {
                'name' : data[0].name,
                'phone' : data[0].phone,
                'password' : data[0].password,
                }
                return JsonResponse(myJson)
        return HttpResponse("oops!")

    except:
        return HttpResponse("wrong2")