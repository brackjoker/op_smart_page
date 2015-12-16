from  data_pool import data_pool
import json
import sys
from django.http import JsonResponse
import re


data_pool_obj = data_pool

def val_set(req):

    if req.method == "POST":
        body_byt = req.body

        print "set create val:"+req.body

        rest_obj = json.loads(body_byt.decode(sys.stdin.encoding))
        if rest_obj['val_type'] == "set":

            if rest_obj in 'flavor_name':
                data_pool_obj.flavor_name = str(rest_obj['flavor_name'])
            elif rest_obj in 'network_name':
                data_pool_obj.network_name = str(rest_obj['flavor_name'])
            elif rest_obj in 'image_name':
                data_pool_obj.image_name = str(rest_obj['flavor_name'])
            elif rest_obj in 'server_name':
                data_pool_obj.server_name = str(rest_obj['server_name'])

            content = {}

        elif rest_obj['val_type'] == "get":

            content = {"flavor_name":data_pool_obj.flavor_name,
                       "network_name":data_pool_obj.network_name,
                       "image_name":data_pool_obj.image_name,
                       "server_name":data_pool_obj.server_name}

        elif  rest_obj['val_type'] == "match":

            if "@hirahara-hubot: [WARNING] Failed to compute_task_build_instances: No valid host was found. There are not enough hosts available." == str(rest_obj['message']):
                print "match"

            elif re.match("@hirahara-hubot: \[WARNING\] Failed to compute_task_build_instances: Timed out waiting for a reply to message ID .*" , str(rest_obj['message'])) != None:
                print "match2"
            else:
                print "none match"
            content = {"message":"match"}



    return JsonResponse(content)
