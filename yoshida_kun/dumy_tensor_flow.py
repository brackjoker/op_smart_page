from django.http import JsonResponse
import sys
import json
from openstack_base import openstack_base
from nova import nova
from flavor import flavor
from make_params import make_params

def exec_operation(req):

    #opbase_obj = openstack_base
    #opbase_obj.password = 'okinawa1940'
    #opbase_obj.username = 'admin'
    #opbase_obj.tenantname = 'admin'

    #opbase_obj.openstack_ip = '192.168.11.22'
    #opbase_obj.get_token()
    #opbase_obj.get_tenant_id()

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
        content = {
                    'instance_id': instance_id,
                    'massage': "rebuild sccess"
                   }

    return JsonResponse(content)


'''
        nova_obj = nova
        nova_obj.getlist(opbase_obj)
        for server_list in nova.server_all_info['servers']:
            if str(server_list['id']) == str(id):
                tmp_data = server_list['flavor']
                target_flavor_id = tmp_data["id"]
                tmp_data = server_list['network']
                network_id = tmp_data["id"]

                image_id = server_list['image']
                tmp_data = server_list['image']
                target_flavor_id = tmp_data["id"]
                break

        flavor_obj = flavor
        flavor_obj.getlist(opbase_obj)
        for server_list in flavor_obj.server_all_info['flavors']:
            if str(server_list['memory']) >= int(memory_size):
                target_flavor_id = str(server_list['id'])
                break


        content = flavor_obj.server_all_info



    print "get instance info networkid,flavorid,imageid,servername"
    print "serch instance flavor"
    print "serch target flavor"
    print "delete instance"
    print "boot instance"
'''