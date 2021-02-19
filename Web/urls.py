"""SchoolOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    re_path(r'^$', views.get_index_page, name='get_index_page'),
    re_path(r'index.html?\??.*', views.get_index_page),   #index.htm或者后面带参数的都可以
    re_path(r'^r_oauth/$', views.r_oauth), # 授权
    re_path(r'^user/$', views.get_user_info), # 获取用户信息
    re_path(r'^MP_verify_pk5McDyW9NG1nDd4.txt$',TemplateView.as_view(template_name="MP_verify_pk5McDyW9NG1nDd4.txt", content_type="text/plain"), name="MP_verify_pk5McDyW9NG1nDd4.txt"),
]

from Web import views as view_error
#配置异常页面
handler403 = view_error.page_permission_denied
handler404 = view_error.page_not_found
handler500 = view_error.page_inter_error