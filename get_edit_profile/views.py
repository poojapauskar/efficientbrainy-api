from register.models import Register
from get_edit_profile.serializers import Get_edit_profileSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404

class Get_edit_profileList(generics.ListCreateAPIView):
 queryset = Register.objects.filter(is_admin=0)
 serializer_class = Get_edit_profileSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

from django.http import JsonResponse

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

class Get_edit_profileUpdate(generics.ListCreateAPIView):
 def get(self, request, *args, **kwargs):
  from django.http import JsonResponse
  # access_token = request.GET.get('access_token')
  pk = request.META.get('HTTP_PK')

  # access_token = '123456789'
  # if(Register.objects.filter(token_generated=access_token).exists()):
  #   pass
  # else:
  #   error=[]
  #   error.append({
  #           'status':'404',
  #           'message':'access token not valid'
  #     })
  #   return JsonResponse(error[0],safe=False)



  # import sys
  # print >> sys.stderr, access_token
  
  Register.objects.filter(pk=pk).update(name=request.META.get('HTTP_NAME'),email=request.META.get('HTTP_EMAIL'),phone=request.META.get('HTTP_PHONE'),city_id=request.META.get('HTTP_CITY'),address=request.META.get('HTTP_ADDRESS'))
    #   return validated_data
  details=[]
  details.append(
                  {
                   'status':200,
                   'message':'Updated',
                  }
                 ) 




  
  return JsonResponse(details[0],safe=False)


       

