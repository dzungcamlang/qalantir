from rest_framework.generics import *

from chrome.models import * ## My model
from chrome.forms import ChromePosts ## my form
from .serializers import ChromeSerializer   ##My serializer

import json
from django.http import HttpResponse
from django.shortcuts import render_to_response,render,redirect
from urlparse import *
import urllib, urllib2
from urllib2 import *

from django.views.decorators.csrf import csrf_exempt


#from .pp import *   Do this later if you want paypal integration

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt



class ChromeListAPIView(ListAPIView):
    queryset= ChromeModel.objects.all()
    serializer_class=ChromeSerializer
class CreateDetailAPIView(CreateAPIView):
    queryset = ChromeModel.objects.all()
    serializer_class=ChromeSerializer
    lookup_field="user"
    lookup_url_kwarg="user"
class UpdateDetailAPIView(UpdateAPIView):
    queryset = ChromeModel.objects.all()
    serializer_class=ChromeSerializer
    lookup_field="user"
    lookup_url_kwarg="user"

@csrf_exempt
def chromepost(request):
    chromedata = {
        'user':request.GET['u'],
        'msg': request.GET['m'],
        }
    form = ChromePosts(
        chromedata
    )
    result=urllib2.urlopen("http://www.qalantir.com/api/chrome/create/", urllib.urlencode(chromedata))
    content= result.read()
    return render(request,"home_templates/home.html",{})
   # return render(request,"homepage_templates/redir.html", {'form': form, 'auth_url': auth_url})
