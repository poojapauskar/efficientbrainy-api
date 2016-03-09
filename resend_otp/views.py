from register.models import Register
from generate_otp.models import Generate_otp
from generate_otp.serializers import Generate_otpSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
import random
from random import randint


from django.http import JsonResponse

class Generate_otpList(generics.ListCreateAPIView):
 queryset = Generate_otp.objects.all()
 serializer_class = Generate_otpSerializer

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)

class Resend_otpList(generics.ListAPIView):
    #paginate_by = 2
    def get(self, request, *args, **kwargs):
      from django.http import JsonResponse

      access_token = request.GET.get('access_token')
      # access_token=''

      import sys
      print >> sys.stderr, access_token

      if(Register.objects.filter(token_generated=access_token).exists()):
        pass
      else:
        error=[]
        error.append({
                'status':'404',
                'message':'access token not valid'
          })
        return JsonResponse(error[0],safe=False)

      import datetime
      now = datetime.datetime.now()
      now_plus_60 = now + datetime.timedelta(minutes = 60)

      user=Register.objects.get(token_generated=access_token)

      if(Generate_otp.objects.filter(user_id=user.pk).exists()):
       Generate_otp.objects.filter(user_id=user.pk).delete() 

      otp_generated=str(random.randint(100000, 999999))
      objects=Generate_otp.objects.create(user_id=user.pk,otp=otp_generated,validity=now_plus_60)


      details=[]
      details.append({
              'status':'200',
              'objects':list(Generate_otp.objects.filter(user_id=user.pk).values('otp','user_id','validity','created'))
        })


      return JsonResponse(details,safe=False)
  	  
class Delete_otp(generics.ListAPIView):
    #paginate_by = 2
    def get(self, request, *args, **kwargs):
      from django.http import JsonResponse

      access_token = request.GET.get('access_token')
      # access_token='123456789'

      import sys
      print >> sys.stderr, access_token

      if(Register.objects.filter(token_generated=access_token).exists()):
        pass
      else:
        error=[]
        error.append({
                'status':'404',
                'message':'access token not valid'
          })
        return JsonResponse(error[0],safe=False)
      
      user=Register.objects.get(token_generated=access_token)
      Generate_otp.objects.filter(user_id=user.pk).delete()



      details=[]
      details.append({
              'status':'200',
              'message':'OTP deleted'
        })


      return JsonResponse(details,safe=False)
  	        
  	  
  	  


       

