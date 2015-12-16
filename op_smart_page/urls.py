"""op_smart_page URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^view/$', 'yoshida_kun.views.test', name='view'),
    url(r'^op_get_info/$', 'op_get_info.op_get_info.getlist', name='op_get_info'),
    url(r'^op_exec_create/$', 'op_exec_create.op_exec_create.exec_create', name='op_exec_create'),
    url(r'^op_exec_delete/$', 'op_exec_delete.op_exec_delete.exec_delete', name='op_exec_delete'),
    url(r'^yoshida_kun/$', 'yoshida_kun.artificial_intelligence_operations.exec_operation', name='yoshida_kun'),
    url(r'^cmd_op/$', 'cmd_exe.cmd_operation.ops_cmd_exec', name='cmd_op'),
    url(r'^val_op/$', 'val_set.val_set.val_set', name='val_op'),
)

"""
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
"""
