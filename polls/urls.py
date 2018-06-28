#! /usr/local/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^time/plus/(\d{1,2})', views.hours_ahead, name='hours_ahead'),
    url(r'^time/',views.current_datetime,name='current_datetime'),
    url('', views.index, name='index'),
]