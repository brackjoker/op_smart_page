import sys
import json
from cmd_op import comand_operation
from django.http import JsonResponse


def ops_cmd_exec(req):


    if req.method == "POST":
        body_byt = req.body
        rest_obj = json.loads(body_byt.decode(sys.stdin.encoding))
        cmd_obj = comand_operation

        #if cmd_obj.chk_str_ascii(str(rest_obj['command'])):

        cmd_obj.cmd_str = str(rest_obj['command'])
        cmd_obj.os_auth_url = 'http://192.168.249.197:35357/v2.0'
        cmd_obj.os_username = 'admin'
        cmd_obj.os_password = 'admin'
        cmd_obj.os_tenant_name = 'admin'

        cmd_obj.make_op_env_val()
        cmd_obj.cmd_exec()

        res_str = cmd_obj.cmd_err_std
        if not res_str :
            res_str = cmd_obj.cmd_out_std

        res_rest_obj = {
                    "command_result": res_str
                    }
        #else:
        #    res_rest_obj = {"message": "error not command"}
    else:
        res_rest_obj = {"message": "error method"}

    return JsonResponse(res_rest_obj)

