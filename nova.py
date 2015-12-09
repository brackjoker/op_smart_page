from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base


class nova:

    result_json = {}
    server_all_info = {}
    nova_rest_result = {}

    #Create Value
    server_name = ""
    image_id = ""
    flavor_num = ""
    network_id = ""
    security_groups = ""
    server_id = ""

    @classmethod
    def getlist(self,ops_base_obj):

        url = 'http://'+ops_base_obj.openstack_ip+':8774/v2/'+ops_base_obj.tenantid+'/servers/detail'
        body = ''
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid}
        resp, token = h.request(url, 'GET', headers=headers, body=body)
        token_body_byt = token
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        self.server_all_info = json.loads(toke_body)

    def get_server_status(self,inst_name):
        inst_status = ""
        for server_list in self.server_all_info['servers']:
            if str(server_list['name']) == str(inst_name):
                inst_status = {"status": str(server_list['status'])}
                break

        return inst_status

    @classmethod
    def create_instance(self,ops_base_obj):

        url = 'http://'+ops_base_obj.openstack_ip+':8774/v2/'+ops_base_obj.tenantid+'/servers'
        body = '{' \
               '"server":{' \
                '"name": "'+self.server_name+'",' \
                '"imageRef": "'+self.image_id+'",' \
                '"flavorRef": "'+self.flavor_num+'",' \
                '"max_count": "1",' \
                '"min_count": "1",' \
                '"networks":' \
                    '[{"uuid": "'+self.network_id+'"}],' \
                '"security_groups":' \
                    '[{"name": "default"}]' \
                '}' \
               '}'

        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid,'Content-Type':'application/json'}
        resp, rest_res = h.request(url, 'POST', headers=headers, body=str(body))

        if "202" == resp.get("status"):
            self.nova_rest_result = {"result":"success"}
        else:
            self.nova_rest_result = {"result":"fail"}
        #result_body_byt = rest_res
        #result_body = result_body_byt.decode(sys.stdin.encoding)
        #self.nova_rest_result = json.loads(result_body)

    @classmethod
    def delete_instance(self,ops_base_obj):
        url = 'http://'+ops_base_obj.openstack_ip+':8774/v2/'+ops_base_obj.tenantid+'/servers/'+self.server_id
        body = ''

        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid,'Content-Type':'application/json'}
        resp, rest_res = h.request(url, 'DELETE', headers=headers, body=body)
        if "204" == resp.get("status"):
            self.nova_rest_result = {"result":"success"}
        else:
            self.nova_rest_result = {"result":"fail"}
#        result_body_byt = rest_res
#        result_body = result_body_byt.decode(sys.stdin.encoding)
#        self.nova_rest_result = json.loads(result_body)

    @classmethod
    def create_value_get(self):

        self.image_id = "2f72eae1-8f3c-4af5-ac08-99ab63a3063b"
        self.flavor_num = "1"
        self.network_id = "6989b58b-d754-468a-ac6e-3058c46efd9c"
        self.security_groups = "default"
        self.server_name = "server-test-2"




"""
            self.result_json = {"servers":[{str(server_list['name']):
                                                {"server_name": str(server_list['name']),
                                                 "status": str(server_list['status']),
                                                 "nova_host": str(server_list['OS-EXT-SRV-ATTR:host'])
                                                 }
                                            }]
                                }
"""
