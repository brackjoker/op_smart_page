from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base


class neutron:

    result_json = {}
    server_all_info = {}

    @classmethod
    def getlist(self,ops_base_obj):

        print "get network info"
        url = 'http://'+ops_base_obj.openstack_ip+':9696/v2.0/networks'
        body = ''
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid}
        resp, token = h.request(url, 'GET', headers=headers, body=body)
        token_body_byt = token
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        self.server_all_info = json.loads(toke_body)
