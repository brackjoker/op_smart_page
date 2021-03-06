from django.http import JsonResponse
import sys
import json
from openstack_base import openstack_base
from nova import nova
from neutron import neutron
from flavor import flavor
from glance import glance
from keystone import keystone

def getlist(req):

    opbase_obj = openstack_base
    opbase_obj.password = 'admin'
    opbase_obj.username = 'admin'
    opbase_obj.tenantname = 'admin'

    #opbase_obj.openstack_ip = '192.168.1.29'
    opbase_obj.openstack_ip = '192.168.249.197'
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
            elif rest_obj['info_type'] == "inst_status":
                content = nova_obj.get_server_status(rest_obj['target_name'])

        elif rest_obj['node_type'] == "neutron":
            neutron_obj = neutron
            neutron_obj.getlist(opbase_obj)
            content = neutron_obj.server_all_info

        elif rest_obj['node_type'] == "flavor":
            flavor_obj = flavor
            flavor_obj.getlist(opbase_obj)
            content = flavor_obj.server_all_info

        elif rest_obj['node_type'] == "glance":
            glance_obj = glance
            glance_obj.getlist(opbase_obj)
            content = glance_obj.server_all_info

        elif rest_obj['node_type'] == "keystone":
            keystone_obj = keystone
            keystone_obj.getlist(opbase_obj)
            content = keystone_obj.server_all_info

        else:
            content = {"message": "ERROR: none info type"}

    return JsonResponse(content)

