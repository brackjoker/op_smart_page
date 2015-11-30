from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base
from nova import nova


def getlist(req):

    if req.method == "POST":
        body_byt = req.body
        rest_obj = json.loads(body_byt.decode(sys.stdin.encoding))

        if rest_obj['type'] == "info":
            print("get info")

        else:
            print("command")

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

