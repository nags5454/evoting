"""evoting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mainapp import views

urlpatterns = [
	url(r'^$',views.home0,name='home0'),
	url(r'^home/(?P<pk>\d+)/$',views.home,name='home'),
    path('admin/', admin.site.urls),
    url(r'^vote/(?P<pk>\d+)/$',views.vote,name='vote'),
    url(r'^electrol/(?P<pk>\d+)/$',views.electrol,name='electrol'),
    url(r'^details/(?P<pk>\d+)/(?P<pku>\d+)/$',views.details,name='details'),
    url(r'^cast/(?P<pkcn>\d+)/(?P<pka>\d+)/(?P<pku>\d+)/$',views.cast,name='cast'),
]
