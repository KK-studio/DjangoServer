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
def SearchDoc(request):
    try:
        print('Raw Data: "%s"' % request.body)
        myJson = json.loads(request.body)
        name = myJson['name']
        check = Doctors.objects
        if (name != None or name !=''):
            check = Doctors.objects.filter(name__contains=name)
        
        print(check)
        specs = myJson['specs']
        data = []
        for i in range(len(specs)):
            if specs[i] is True:
                data.append(check.filter(spec=i))
        if len(data) == 0:
            data.append(check)

        myList = []
        print("why" + str(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                myJson = {
                'name' : data[i][j].name,
                'phone' : data[i][j].phone,
                'spec' : data[i][j].spec,
                'number' : data[i][j].number,
                'online_pay' : data[i][j].online_pay,
                'experience_years' : data[i][j].experience_years,
                'address' : data[i][j].address,
                'week_days' : data[i][j].week_days,
                'last_Comment' : data[i][j].last_Comment,
                'scores_count' : data[i][j].scores_count,
                }
                if data[i][j].scores_count != 0:
                    myJson['score'] = data[i][j].total_scores_sum / data[i][j].scores_count
                else:
                    myJson['score'] = 0
                myList.append(myJson)
                print("hi")
        result = {'result' : myList} 
        return JsonResponse(result)
        
    except:
        return HttpResponse("None")





@csrf_exempt
def getDoc(request,text):
    try:
        print('GET Raw Data: "%s"' % text)

        phone = text
        if Doctors.objects.filter(phone=phone).exists():
            data = Doctors.objects.filter(phone=phone)
            comments = []
            if Comments.objects.filter(doc_phone=phone).exists:
                data2 = Comments.objects.filter(doc_phone=phone)
                for i in range(len(data2)):
                    newJson = {
                        'name':data2[i].name,
                        'comment':data2[i].comment,
                        'score' : data2[i].score
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
            'last_Comment' : data[0].last_Comment,
            'scores_count' : data[0].scores_count,
            'comments' : comments
            }
            if data[0].scores_count != 0:
                myJson['score'] = data[0].total_scores_sum / data[0].scores_count
            else:
                myJson['score'] = 0
            return JsonResponse(myJson)
        return HttpResponse("None")
    except:
        return HttpResponse("wrong2")



@csrf_exempt
def addComment(request):
    try:
        print('GET Raw Data: "%s"' % request.body)
        myJson = json.loads(request.body)
        doc_phone = myJson['doc_phone']
        phone = myJson['phone']
        comment = myJson['comment']
        score = myJson['score']
        if User.objects.filter(phone=phone).exists():
            print("why")
            if Doctors.objects.filter(phone=doc_phone).exists():
                
                name = User.objects.filter(phone=phone)[0].name
                doc = Doctors.objects.filter(phone=doc_phone)[0]
                newCooment = Comments(doc_phone=doc,name = name,comment=comment,score=score)
                doc.last_Comment = comment
                doc.scores_count += 1
                doc.total_scores_sum += score
                newCooment.save()
                data2 = Comments.objects.filter(doc_phone=doc)
                comments = []
                for i in range(len(data2)):
                    newJson = {
                        'name':data2[i].name,
                        'comment':data2[i].comment,
                        'score' : data2[i].score
                    }
                    comments.append(newJson)
                # myJson = {
                # 'name' : data[0].name,
                # 'phone' : data[0].phone,
                # 'password' : data[0].password,
                # }
                # return JsonResponse(myJson)
                result = {'comments':comments}
                return JsonResponse(result)
        return HttpResponse("None")

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