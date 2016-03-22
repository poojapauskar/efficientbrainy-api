from register.models import Register
# from login.serializers import LoginSerializer
from rest_framework import generics

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

class Update_logged_inList(generics.ListCreateAPIView):
 def get(self, request, *args, **kwargs):
  logged_in=request.META.get('HTTP_LOGGED_IN')
  
  Register.objects.filter(is_admin=1).update(logged_in=logged_in)
  details=[]
  details.append(
                  {
                   'status':200,
                  }
                 )  

  import sys
  from django.http import JsonResponse
  return JsonResponse(details[0],safe=False)

class Check_logged_inList(generics.ListCreateAPIView):
 def get(self, request, *args, **kwargs):
  
  obj=Register.objects.get(is_admin=1)
  details=[]

  if(obj.logged_in=="1"):
   details.append(
                  {
                   'status':200,
                  }
                 )
  else:
   details.append(
                  {
                   'status':400,
                  }
                 )

  import sys
  from django.http import JsonResponse
  return JsonResponse(details[0],safe=False)