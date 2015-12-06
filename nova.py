from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base


class nova:

    result_json = {}
    server_all_info = {}

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

    def get_server_info(self,json_obj):
        for server_list in json_obj['servers']:

            self.result_json = {"servers":[{str(server_list['name']):
                                                {"server_name": str(server_list['name']),
                                                 "status": str(server_list['status']),
                                                 "nova_host": str(server_list['OS-EXT-SRV-ATTR:host'])
                                                 }
                                            }]
                                }
