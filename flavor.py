from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base


class flavor:

    result_json = {}
    server_all_info = {}

    @classmethod
    def getlist(self,ops_base_obj):

        url = 'http://'+ops_base_obj.openstack_ip+':8774/v2/'+ops_base_obj.tenantid+'/flavors'
        body = ''
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid}
        resp, token = h.request(url, 'GET', headers=headers, body=body)
        token_body_byt = token
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        self.server_all_info = json.loads(toke_body)

    def get_name(self,flavor_id):

        flavor_name = ""
        for flavor_list in self.server_all_info['flavors']:
            if str(flavor_list['id']) == str(flavor_id):
                flavor_name = str(flavor_list['name'])
                break

        return flavor_name
