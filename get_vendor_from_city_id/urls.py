from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from get_vendor_from_city_id import views
#from get_list.views import get_queryset

urlpatterns = [
    url(r'^get_vendor_from_city_id/?id=(?P<id>(\w+))/$', views.CustomListView.as_view()),
    #url(r'^get_list/$', get_queryset),
    #url(r'^get_list/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]