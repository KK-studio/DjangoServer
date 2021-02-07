from django.contrib import admin

# Register your models here.
from .models import Question,Doctors,User,Comments
admin.site.register(Question)
admin.site.register(Doctors)
admin.site.register(User)
admin.site.register(Comments)
