from django.http import JsonResponse
import sys
import httplib2
import json
from nova import nova
from neutron import neutron
from flavor import flavor
from glance import glance

class make_params:

    opbase_obj = ""

    #Create Value
    image_id = ""
    flavor_num = ""
    network_id = ""
    server_id = ""
    server_name = ""

    @classmethod
    def get_flavor_ref(self, flavor_name):

        flavor_obj = flavor
        flavor_obj.getlist(self.opbase_obj)
        flavor_info = flavor_obj.server_all_info

        for flavor_element in flavor_info['flavors']:
            if str(flavor_element['name']) == flavor_name:
                self.flavor_num = str(flavor_element['id'])
                break

    @classmethod
    def get_image_id(self, image_name):

        glance_obj = glance
        glance_obj.getlist(self.opbase_obj)
        image_info = glance_obj.server_all_info
        for image_element in image_info['images']:
            if str(image_element['name']) == image_name:
                self.image_id = str(image_element['id'])
                break

    @classmethod
    def get_network_id(self, net_name):

        neutron_obj = neutron
        neutron_obj.getlist(self.opbase_obj)
        net_info = neutron_obj.server_all_info
        for net_element in net_info['networks']:
            if str(net_element['name']) == net_name:
                self.network_id = str(net_element['id'])
                break

    @classmethod
    def get_server_id(self, nova_name):
        nova_obj = nova
        nova_obj.getlist(self.opbase_obj)
        nova_info = nova_obj.server_all_info
        for nova_element in nova_info['servers']:
            if str(nova_element['name']) == nova_name:
                self.server_id = str(nova_element['id'])
                break

    @classmethod
    def get_server_name(self, server_id):
        nova_obj = nova
        nova_obj.getlist(self.opbase_obj)
        nova_info = nova_obj.server_all_info
        for nova_element in nova_info['servers']:
            if str(nova_element['id']) == server_id:
                self.server_name = str(nova_element['name'])
                break

    @classmethod
    def delete_value_get(self, nova_obj):
        self.get_server_id(self.server_name)
        nova_obj.server_id = self.server_id

    @classmethod
    def create_value_get(self, nova_obj, flavor_name, image_name, network_name):

        self.get_flavor_ref(flavor_name)
        self.get_image_id(image_name)
        self.get_network_id(network_name)

        nova_obj.image_id = self.image_id
        nova_obj.flavor_num = self.flavor_num
        nova_obj.network_id = self.network_id

"""
        self.image_id = "2f72eae1-8f3c-4af5-ac08-99ab63a3063b"
        self.flavor_num = "1"
        self.network_id = "6989b58b-d754-468a-ac6e-3058c46efd9c"
        self.security_groups = "default"
        self.server_name = "server-test-2"
"""
