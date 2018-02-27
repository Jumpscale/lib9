# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
from .Task import Task
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError




class BlueprintsService:
    def __init__(self, client):
        self.client = client
        pass

    def ExecuteBlueprint(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Execute a blueprint on the ZeroRobot
        It is method for POST /blueprints
        """
        uri = self.client.base_url + "/blueprints"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append(Task(elem))
                return resps, resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)
