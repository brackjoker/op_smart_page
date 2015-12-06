from django.http import JsonResponse
import sys
import json
from openstack_base import openstack_base
from nova import nova


def getlist(req):

    opbase_obj = openstack_base
    opbase_obj.password = 'okinawa1940'
    opbase_obj.username = 'admin'
    opbase_obj.tenantname = 'admin'

    opbase_obj.openstack_ip = '192.168.151.202'
    opbase_obj.get_token()
    opbase_obj.get_tenant_id()

    if req.method == "POST":
        body_byt = req.body
        rest_obj = json.loads(body_byt.decode(sys.stdin.encoding))

        if rest_obj['type'] == "nova":
            nova.getlist(opbase_obj)


        elif rest_obj['type'] == "neutron":
            print("command")




    content = {"rest": "OK"}



    return JsonResponse(content)

