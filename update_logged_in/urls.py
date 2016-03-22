from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from update_logged_in import views

urlpatterns = [
    url(r'^update_logged_in/$', views.Update_logged_inList.as_view()),
    url(r'^update_logged_in/check/$', views.Check_logged_inList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)