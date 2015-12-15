from django.http import JsonResponse
import sys
import json
from openstack_base import openstack_base
from nova import nova
from make_params import make_params

def exec_delete(req):

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
            nova_obj.nova_rest_result = {}

            if rest_obj['exec_type'] == "inst_delete":
                params_obj = make_params
                params_obj.opbase_obj = opbase_obj
                if "server_name" in rest_obj:
                    params_obj.server_name = str(rest_obj['server_name'])
                    params_obj.delete_value_get(nova_obj)
                #nova_obj.create_value()
                else:
                    params_obj.server_id = str(rest_obj['server_id'])
                    params_obj.get_server_name(str(rest_obj['server_id']))

                nova_obj.delete_instance(opbase_obj)
                content = nova_obj.nova_rest_result

        elif rest_obj['node_type'] == "neutron":
            print 0

        elif rest_obj['node_type'] == "flavor":
            print 0

        elif rest_obj['node_type'] == "glance":
            print 0

        elif rest_obj['node_type'] == "keystone":
            print 0

        else:
            content = {"massage": "ERROR: none exec type"}

    return JsonResponse(content)

