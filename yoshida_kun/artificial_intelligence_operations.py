from django.http import JsonResponse
import sys
import json
from openstack_base import openstack_base
from nova import nova
from flavor import flavor
from glance import glance
from make_params import make_params
from text_classifier import text_classifier
from cmd_op import comand_operation
from file_function import file_function


def exec_operation(req):

    opbase_obj = openstack_base
    opbase_obj.password = 'admin'
    opbase_obj.username = 'admin'
    opbase_obj.tenantname = 'admin'

    #opbase_obj.openstack_ip = '192.168.1.29'
    opbase_obj.openstack_ip = '192.168.249.197'
    opbase_obj.get_token()
    opbase_obj.get_tenant_id()

    target_image_name = ""
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
#        if str(instance_id) != "" :

        file_function.make_tensor_file(str(rest_obj['massage1']))

        cmd = text_classifier.exec_tensor()
        #cmd = "rebuild"
        
        if cmd == "none":
            content = {
                    'massage': "",
                    'err_massage': "operation is no command"
                   }
        elif cmd == "rebuild":
            content = exec_rebuild(opbase_obj,instance_id)
        else:
            cmd_obj = comand_operation
            cmd_obj.cmd_str = str(cmd)
            cmd_obj.os_auth_url = 'http://192.168.249.197:35357/v2.0'
            cmd_obj.os_username = 'admin'
            cmd_obj.os_password = 'admin'
            cmd_obj.os_tenant_name = 'admin'
            cmd_obj.make_op_env_val()
            cmd_obj.cmd_exec()
#        else:
    #        content = exec_rebuild(opbase_obj,instance_id)
#            print 0
            content = {
                        'massage': cmd_obj.cmd_out_std,
                        'err_massage': cmd_obj.cmd_err_std
                       }

    return JsonResponse(content)


def exec_rebuild(opbase_obj,instance_id):
    nova_obj = nova
    nova_obj.getlist(opbase_obj)
    params_obj = make_params
    params_obj.opbase_obj = opbase_obj

    flavor_name = ""
    net_name = ""
    image_id = ""
    image_name = ""

    for server_list in nova.server_all_info['servers']:
        #"serch instance flavor"
        if str(server_list['id']) == str(instance_id):
            #tmp_data = server_list['flavor']
            #target_flavor_id = tmp_data["id"]
            tmp_data = server_list['image']
            image_id = tmp_data["id"]
            break

    glance_obj = glance
    glance.getlist(opbase_obj)
    target_image_name = glance.get_name(image_id)

    print "netwoekID serch function"
    net_name = "public"

    print "serch target flavor"
    #flavor_obj = flavor
    #flavor_obj.getlist(opbase_obj)
    #content = flavor_obj.server_all_info
    #get flavor name
    flavor_name = "m1.small"


    print "delete instance"
    params_obj.server_id = str(instance_id)
    params_obj.get_server_name(str(instance_id))
    nova_obj.server_id = params_obj.server_id
    nova_obj.server_name = params_obj.server_name
    nova_obj.delete_instance(opbase_obj)

    print "boot instance"
    params_obj.create_value_get(nova_obj, flavor_name, target_image_name, net_name)
    nova_obj.server_name = str(params_obj.server_name)
    nova_obj.create_instance(opbase_obj)
    content = nova_obj.nova_rest_result
#    content = {
#                'instance_id': instance_id,
#                'massage': "rebuild sccess"
#               }
    return content