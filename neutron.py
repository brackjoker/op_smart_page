from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base


class neutron:

    result_json = {}

    @classmethod
    def getlist(self,ops_base_obj):

        url = 'http://'+ops_base_obj.openstack_ip+':9696/v2.0/networks'
        body = ''
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid}
        resp, token = h.request(url, 'GET', headers=headers, body=body)
        token_body_byt = token
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        server_info = json.loads(toke_body)

        for server_list in server_info['servers']:

            result_json = {"server_name": str(server_list['name']),"nova_host": str(server_list['OS-EXT-SRV-ATTR:host']),"network":[]}
            print("server name: ",str(server_list['name']))
            print("nova host: ",str(server_list['OS-EXT-SRV-ATTR:host']))
            i=0
            for network_obj in server_list['addresses']:
                result_json.update({"network":[{"address" : network_obj}]})
                print(network_obj)
                i = i + 1