from register.models import Register
from generate_otp.models import Generate_otp
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
    #paginate_by = 2
    def get(self, request, *args, **kwargs):
     

      import sys
      # print >> sys.stderr, service_id
      user_id=request.META.get('HTTP_ID')
      user=Register.objects.get(pk=user_id)
      otp=list(Generate_otp.objects.filter(user_id=user_id).values('otp'))
      file_no=list(Generate_otp.objects.filter(user_id=user_id).values('file_no'))
      

      details=[]
      details.append({
      		'status':200,
          'otp':otp,
          'vendor_name':user.name,
          'vendor_username':user.username,
          'vendor_id':user.pk,
          'file_no':file_no,
        })
      
      return JsonResponse(details[0],safe=False)
  