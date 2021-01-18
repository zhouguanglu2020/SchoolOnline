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
  host('www', settings.ROOT_URLCONF, name='www'), # `name`与`DEFAULT_HOST` 相同
  host('api', 'Api.urls', name='api'),
  host('app', 'Application.urls', name='app'),
  host('we', 'Wechat.urls', name='wechat'),
  host('blog', 'Blog.urls', name='blog'),
)