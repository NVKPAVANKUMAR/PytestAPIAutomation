import json
import os

ROOT_DIR = os.path.abspath(os.curdir)
ENDPOINTS_FILE = os.path.join(ROOT_DIR, "api", "endpoints.json")


class FileClass:

    def get_property_from_file(name):
        try:
            with open(ENDPOINTS_FILE) as json_file:
                data = json.load(json_file)
            return data[name]
        except(FileNotFoundError, KeyError) as e:
            raise Exception("Error when try to get the property from file: " + str(e))

    def build_url(endpoint):
        try:
            base_url = FileClass.get_property_from_file('BASE_URL')
            return base_url + endpoint
        except Exception as e:
            raise Exception("Error when try to build the URL: " + str(e))
