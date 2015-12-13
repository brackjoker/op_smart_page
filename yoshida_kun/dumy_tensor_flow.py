from django.http import JsonResponse
import sys
import json
from openstack_base import openstack_base
from nova import nova
from flavor import flavor
from make_params import make_params

def exec_operation(req):

    opbase_obj = openstack_base
    opbase_obj.password = 'admin'
    opbase_obj.username = 'admin'
    opbase_obj.tenantname = 'admin'

    opbase_obj.openstack_ip = '192.168.249.197'
    opbase_obj.get_token()
    opbase_obj.get_tenant_id()

    target_flavor_id = ""
    network_id = ""
    image_id = ""
    server_name = ""
    tmp_data = {}
    memory_size = 0
    instance_id = ""

    if req.method == "POST":
        body_byt = req.body
        rest_obj = json.loads(body_byt.decode(sys.stdin.encoding))
        instance_id = rest_obj['instance_id']

#        content = exec_rebuild(opbase_obj,instance_id)
        content = {
                    'instance_id': instance_id,
                    'massage': "rebuild sccess"
                   }


    return JsonResponse(content)


def exec_rebuild(opbase_obj,instance_id):
    nova_obj = nova
    nova_obj.getlist(opbase_obj)
    params_obj = make_params
    params_obj.opbase_obj = opbase_obj

    flavor_name = ""
    net_name = ""
    image_name = ""

    for server_list in nova.server_all_info['servers']:
        #"serch instance flavor"
        if str(server_list['id']) == str(id):
            #tmp_data = server_list['flavor']
            #target_flavor_id = tmp_data["id"]
            tmp_data = server_list['image']
            target_flavor_id = tmp_data["id"]
            break

    #get flavor name
    flavor_name = "m1.tiny"


    print "netwoekID serch function"
    net_name = "public"

    print "serch target flavor"
    flavor_obj = flavor
    flavor_obj.getlist(opbase_obj)
    content = flavor_obj.server_all_info

    print "delete instance"
    params_obj.server_id = str(instance_id)
    params_obj.get_server_name(str(instance_id))
    nova_obj.delete_instance(opbase_obj)

    print "boot instance"
    params_obj.create_value_get(nova_obj, flavor_name, image_name, net_name)
    nova_obj.server_name = str(params_obj)
    nova_obj.create_instance(opbase_obj)
    content = nova_obj.nova_rest_result
    content = {
                'instance_id': instance_id,
                'massage': "rebuild sccess"
               }
    return content