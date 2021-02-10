# -*- coding: utf-8 -*-
"""
@Time : 2021/1/17 23:12
@Author : Administrator
@Email : zhouguanglu2012@163.com
@File : hosts.py
@Project : OnlineSchool
@Description：站点分URL
"""
from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
  host(r'(www|)', 'Web.urls', name='www'), # `name`与`DEFAULT_HOST` 相同
  host(r'api', 'Api.urls', name='blog'),
)

