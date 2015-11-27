from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base
from nova import nova


def getlist(req):

    opbase_obj = openstack_base
    opbase_obj.password = 'admin'
    opbase_obj.username = 'admin'
    opbase_obj.tenantname = 'admin'

    opbase_obj.openstack_ip = '172.20.2.59'
    opbase_obj.get_token()
    opbase_obj.get_tenant_id()
    nova.getlist(opbase_obj)

    content = {"rest": "OK"}



    return JsonResponse(content)

