"""openSource URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from openSource.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^camera/', include('camera.urls', namespace='camera')),
    # url(r'^crimer/', include('crimer.urls', namespace='crimer')),
    # url(r'^community/', include('community.urls', namespace='community')),
    url(r'^introduce/', include('introduce.urls', namespace='introduce')),
    url(r'^com/', include('jejudaum.urls', namespace='jejudaum')),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),


    url(r'^$', HomeView.as_view(), name='home'),
]
