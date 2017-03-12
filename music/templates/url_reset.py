from django.conf.urls import url_reset
from django.contrib.auth.views import password_reset, password_reset_done
#from django.contrib.auth.views import *
#from django.contrib.auth.views import password_reset, password_reset_done
#from django.views.generic import direct_to_template
admin.autodiscover()

app_name = 'music'

urlpatterns = [
    
    url(r'^primeiralei/$', views.primeiralei, name='primeiralei'),
    url(r'^primeiralei_resultado/$', views.primeiralei_resultado, name='primeiralei_resultado'),
    



]

