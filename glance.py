from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base


class glance:

    result_json = {}
    server_all_info = {}

    @classmethod
    def getlist(self,ops_base_obj):

        url = 'http://'+ops_base_obj.openstack_ip+':9292/v2/images'
        body = ''
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid}
        resp, token = h.request(url, 'GET', headers=headers, body=body)
        token_body_byt = token
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        self.server_all_info = json.loads(toke_body)


    @classmethod
    def get_name(self,image_id):
        for server_list in self.server_all_info['images']:
            if str(server_list['id']) == image_id:
                image_name = str(server_list['name'])
                break
        return image_name
"""
    def get_server_status(self,inst_name):
        inst_status = ""
        for server_list in self.server_all_info['servers']:
            if str(server_list['name']) == inst_name:
                inst_status = {"status": str(server_list['status'])}
                break

        return inst_status

    @classmethod
    def create_instance(self):
        print 0
"""

"""
            self.result_json = {"servers":[{str(server_list['name']):
                                                {"server_name": str(server_list['name']),
                                                 "status": str(server_list['status']),
                                                 "nova_host": str(server_list['OS-EXT-SRV-ATTR:host'])
                                                 }
                                            }]
                                }
"""