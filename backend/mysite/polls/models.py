from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):
    phone = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class Doctors(models.Model):
    phone = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200,null=False)
    name = models.CharField(max_length=200)
    spec = models.IntegerField(default=0)
    number = models.CharField(max_length=200)
    online_pay = models.BooleanField(default=False)
    experience_years = models.IntegerField(default=0)
    address = models.CharField(max_length=1000,default="none")
    week_days = models.TextField(max_length=1000,default="[false,false,false,false,false,false,false]")
    total_scores_sum = models.IntegerField(default=0)
    scores_count = models.IntegerField(default=0)
    last_Comment = models.TextField(max_length=500,default="no comments!")


class Comments(models.Model):
    comment = models.CharField(max_length=500,null=False)
    doc_phone = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    name = models.CharField(max_length=500,null=False) 
    