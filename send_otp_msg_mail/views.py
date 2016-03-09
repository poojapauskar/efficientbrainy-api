
from register.models import Register
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 
from django.http import JsonResponse

# class Get_listList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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

from django.views import generic
from django.views.generic import ListView

class CustomListView(ListView):
 def get(self, request, *args, **kwargs):

  # in headers CREDIT-CARD-NO
  import sys
  user_id= request.META.get('HTTP_ID')
  user_otp= request.META.get('HTTP_OTP')

  user=Register.objects.get(pk=user_id)
  
  from pprint import pprint
  import requests
  from django.conf import settings

  sid = 'bitjini'
  token = '85dbbbc18dfaf078290eeee3c185ac6dfd8a208f'

  def send_message(sid, token, sms_from, sms_to, sms_body):
	    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
	    auth=(sid, token),
	    data={
	        'From': sms_from,
	        'To': sms_to,
	        'Body': sms_body
	    })





  import sys
  msg="OTP generated "+user_otp

 
  import sys 
  print >> sys.stderr, msg


  
  r = send_message(sid, token,
	    sms_from='09243422233',  # sms_from='8808891988',
	    sms_to=user.phone, # sms_to='9052161119',
	    sms_body=msg)
  print r.status_code
  pprint(r.json())


  from django.core.mail import send_mail
  send_mail('SAVMYTIME: ',msg, 'poojapauskar22@gmail.com', [user.email], fail_silently=False)



  
  details=[]

  details.append(
	          {
	           'status':200,
	          }
	         )
  
  return JsonResponse(details,safe=False)
  