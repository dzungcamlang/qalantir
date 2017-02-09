"""qalantir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login
####
from home import views as home_views

from speech import views as speech_views

####
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^speech/$',speech_views.speechHome,name="speech"),
    url(r'^BND/(?P<path>.*)$',speech_views.BND,name="BND"),
    # url(r'^speech/$',speech_views.speechHome,name="speech"),
    url(r'^granite/$',speech_views.speechHome,name="speechHomeGranite"),
    url(r'^granite/(?P<id>\d+)/$',speech_views.speechGranite,name="speechGranite"),
    url(r'^capitalism/$',speech_views.capitalism,name="capitalism"),
    url(r'^$',home_views.home,name="home")
    
]

urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) # for json uploads
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # for json uploads

