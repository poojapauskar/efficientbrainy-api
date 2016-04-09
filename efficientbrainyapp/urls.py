"""efficientbrainyapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^', include('register.urls')),
    url(r'^', include('login.urls')),
    url(r'^', include('generate_otp.urls')),
    url(r'^', include('resend_otp.urls')),
    url(r'^', include('valid_otp.urls')),
    url(r'^', include('check_username.urls')),
    url(r'^', include('city.urls')),
    url(r'^', include('get_edit_city.urls')),
    url(r'^', include('get_edit_profile.urls')),
    url(r'^', include('is_admin_login.urls')),
    url(r'^', include('get_city_from_id.urls')),
    url(r'^', include('delete_user.urls')),
    url(r'^', include('delete_city.urls')),
    url(r'^', include('get_vendor_from_city_id.urls')),
    url(r'^', include('send_otp_msg_mail.urls')),
    url(r'^', include('get_otp_from_user_id.urls')),
    url(r'^', include('update_logged_in.urls')),
)



# urlpatterns = [
#     url(r'^', include('register.urls')),
#     url(r'^', include('login.urls')),
#     url(r'^', include('generate_otp.urls')),
#     url(r'^', include('resend_otp.urls')),
#     url(r'^', include('valid_otp.urls')),
#     url(r'^', include('check_username.urls')),
#     url(r'^', include('city.urls')),
#     url(r'^', include('get_edit_city.urls')),
#     url(r'^', include('get_edit_profile.urls')),
# ]
