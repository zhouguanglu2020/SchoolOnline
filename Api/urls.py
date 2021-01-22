# -*- coding: utf-8 -*-
"""
@Time : 2021/1/21 8:02
@Author : Administrator
@Email : zhouguanglu2012@163.com
@File : urls.py
@Project : SchoolOnline
@Description：
"""
from django.urls import path,re_path
from Api import  views

urlpatterns = [
    path('', views.zhwdsb,name='dsb'),
    re_path(r'^index.html$',views.zhwdsb2,name='dsb2')
]
