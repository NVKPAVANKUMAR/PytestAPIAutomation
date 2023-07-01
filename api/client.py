import json

import requests


class APIClient:
    def __init__(self, base_url=None):
        self.base_url = self.get_url_base()

    def get_url_base(self):
        with open('api/endpoints.json') as json_file:
            data = json.load(json_file)
        return data['BASE_URL']

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, data=None, json=None):
        url = self.base_url + endpoint
        response = requests.post(url, data=data, json=json)
        return response

    def put(self, endpoint, data=None, json=None):
        url = self.base_url + endpoint
        response = requests.put(url, data=data, json=json)
        return response

    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url)
        return response
