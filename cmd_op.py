import subprocess
import re

class comand_operation:

    cmd_str = ''
    cmd_res = ''
    cmd_exec_code = ''
    cmd_bf_str = ''
    cmd_af_str = ''

    cmd_out_std = ''
    cmd_err_std = ''

    password = ''
    os_username = ''
    os_password = ''
    os_tenant_name = ''
    os_auth_url = ''

    @classmethod
    def chk_str_ascii(self,str):
        regexp = re.compile(str)
        result = regexp.search(" abcdefghijklmnopqrstuvwxyz!#$&'-*()[]@")
        return_res = False
        if result == None :
            return_res = False
        else :
            return_res = True
        return return_res

    @classmethod
    def cmd_exec(self):
        com = str(self.cmd_bf_str) + str(self.cmd_str) + str(self.cmd_af_str)
        print(com)
        self.cmd_res = subprocess.Popen(com, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.cmd_out_std = self.cmd_res.stdout.readlines()
        self.cmd_err_std = self.cmd_res.stderr.readlines()

        print('result stdout:' + str(self.cmd_res.stdout.readlines()))
        print('result stderr:' + str(self.cmd_res.stderr.readlines()))

    @classmethod
    def make_op_env_val(self):

        self.cmd_bf_str = 'export OS_AUTH_URL="' + self.os_auth_url + '" && export OS_USERNAME="'+self.os_username+'" && export OS_PASSWORD="'+self.os_password+'" && export OS_TENANT_NAME="'+self.os_tenant_name+'" && '
