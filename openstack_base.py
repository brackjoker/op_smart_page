import httplib2
import json
import sys

class openstack_base:
    openstack_ip = ''
    username = ''
    password = ''
    tenantname = ''
    tokenid = ''
    tenantid = ''
    @classmethod
    def get_token(self):
        url = 'http://'+self.openstack_ip+':5000/v2.0/tokens'
        body = '{"auth": {"tenantName": "' + str(self.tenantname) + '", "passwordCredentials": {"username": "'+ str(self.username)+'", "password": "'+str(self.password)+'"}}}'
        headers = {'Content-Type': 'application/json'}

        h = httplib2.Http(timeout=30)
        resp, token = h.request(url, 'POST', headers=headers, body=body)
        token_body_byt = token
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        token_id_dic = json.loads(toke_body)
        self.tokenid = token_id_dic['access']['token']['id']
        return

    @classmethod
    def get_tenant_id(self):

        url = 'http://'+self.openstack_ip+':5000/v2.0/tenants'
        body = ''
        #body = '{"auth": {"tenantName": "' + str(self.tenantname) + '", "passwordCredentials": {"username": "'+ str(self.username)+'", "password": "'+str(self.password)+'"}}}'
        headers = {'Content-Type': 'application/json','X-Auth-Token': self.tokenid, 'Accept': 'application/json'}

        h = httplib2.Http(timeout=30)
        resp, token = h.request(url, 'GET', headers=headers, body=body)
        token_body_byt = token
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        tenant_dic = json.loads(toke_body)
        l = tenant_dic['tenants']
        for tenant_list in tenant_dic['tenants']:
            if str(tenant_list['name']) == str(self.tenantname):
                self.tenantid = tenant_list['id']
        return

