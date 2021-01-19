# -*- coding: utf-8 -*-
"""
@Time : 2021/1/19 10:32
@Author : Administrator
@Email : zhouguanglu2012@163.com
@File : database_router.py
@Project : SchoolOnline
@Description： 表示路由返回的数据库
"""
from django.conf import settings

DBList = settings.DATABASES.keys()

class DatabaseAppsRouter(object):
    """
    A router to control all database operations on models for different
    databases.

    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.

    Settings example:

    直接使用app_label，作为返回数据库的名称。
    """

    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in DBList:
            return model._meta.app_label
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta.app_label in DBList:
            return model._meta.app_label
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""

        if obj1._meta.app_label in DBList and obj2._meta.app_label in DBList:
            return True
        return None