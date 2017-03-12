from django.conf.urls import url
from . import views
from django.contrib.auth.views import password_reset, password_reset_done
#from django.contrib.auth.views import *
#from django.contrib.auth.views import password_reset, password_reset_done
#from django.views.generic import direct_to_template


app_name = 'music'

urlpatterns = [
    
    #url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done')


]

