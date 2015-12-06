from django.http import JsonResponse
import sys
import json
from openstack_base import openstack_base
from nova import nova
from neutron import neutron
from flavor import flavor

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

        if rest_obj['node_type'] == "nova":
            nova_obj = nova
            nova_obj.getlist(opbase_obj)

            if rest_obj['info_type'] == "all_info":
                content = nova_obj.server_all_info
            else:
                content = nova_obj.get_server_status(str(rest_obj['target_name']))

        elif rest_obj['node_type'] == "neutron":
            neutron_obj = neutron
            neutron_obj.getlist(opbase_obj)
            content = neutron_obj.server_all_info

        elif rest_obj['node_type'] == "flavor":
            flavor_obj = flavor
            flavor_obj.getlist(opbase_obj)
            content = flavor_obj.server_all_info

        else:
            content = {"massage": "ERROR: none info type"}

    return JsonResponse(content)

