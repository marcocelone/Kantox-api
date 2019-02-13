import requests
import json
from config_files import setup



class REQ():

    def __init__(self):

        self.req = requests.Session()


    def get_token(self, login, password, endpoint):

        payload = {"login": login, "password": password}
        token = self.req.post(setup.base_url+endpoint, headers=setup.headers, data=json.dumps(payload))
        response_code = token.status_code
        response_boby = token.json()

        return [response_code, response_boby]

    def get(self, base_url, endpoint, my_token):
        """
        This method is used to make a GET request the token and the endpoint are needed
        """
        request_header = {'Content-Type':'application/json','AUTHORIZATION': my_token}
        result = self.req.get(base_url+endpoint, headers=request_header)
        rs_code = result.status_code
        rs_body = result.json()

        return [rs_code, rs_body]

    def get_body(self, base_url, endpoint, payload, my_token):
        """
        This method is used to make a Get  request the token, endpoint and body are needed
        """
        request_header = {'Accept':'application/json','Content-Type': 'application/json', 'AUTHORIZATION': my_token}
        result = self.req.get(base_url+endpoint, headers=request_header, data=json.dumps(payload))
        rs_code = result.status_code
        rs_body = result.json()

        return [rs_code, rs_body]

    def post(self, base_url, endpoint, payload, my_token):
        """
        This method is used to make a POST  request the token and the endpoint are needed
        """
        request_header = {'Accept':'application/json','Content-Type': 'application/json', 'AUTHORIZATION': my_token}
        result = self.req.post(base_url+endpoint, headers=request_header, data=json.dumps(payload))
        rs_code = result.status_code
        rs_body = result.json()

        return [rs_code, rs_body]

