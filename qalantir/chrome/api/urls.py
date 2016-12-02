from django.conf.urls import include, url 
from django.contrib import admin

from urlparse import parse_qs, urlparse

from .views import *




from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView
from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView



#url = 'example.com/sellerid/?restaurant=mamatacos&food=taco&drink' 
#parsed = urlparse(url) # components; use parsed.query to get everything after ?
#params = parse_qs(parsed.query) # params is a dictionary

urlpatterns=[
    
    url(r'^$', ChromeListAPIView.as_view(), name='list'),

    # url(r'^create/$', CreateDetailAPIView.as_view(), name='create'),
    # url(r'^update/$', UpdateDetailAPIView.as_view(), name='update'),
    # url(r'^destroy/$', DestroyDetailAPIView.as_view(), name='destroy'),
    # url(r'^(?P<company>[\w-]+)/$', ChromeDetailAPIView.as_view(), name='detail'),
    # url(r'^(?P<company>[\w-]+)/destroy/$', DestroyDetailAPIView.as_view(), name='destroy'),
    # url(r'^(?P<company>[\w-]+)/update/$', UpdateDetailAPIView.as_view(), name='update'),
  

             #url(r'^api-buy/(.+)/([0-9]{10})/([0-9]+)/$', views.article_detail)
]