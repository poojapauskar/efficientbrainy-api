from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from is_admin_login import views

urlpatterns = [
    url(r'^is_admin_login/$', views.Is_admin_loginList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)