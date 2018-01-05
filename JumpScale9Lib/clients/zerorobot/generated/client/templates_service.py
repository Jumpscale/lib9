
from .Template import Template
from .api_response import APIResponse
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class TemplatesService:
    def __init__(self, client):
        self.client = client

    def ListTemplates(self, headers=None, query_params=None, content_type="application/json"):
        """
        List all the templates available to the ZeroRobot
        It is method for GET /templates
        """
        uri = self.client.base_url + "/templates"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append(Template(elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def AddTemplateRepo(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Clone a template repository and make the templates available to the ZeroRobot
        It is method for POST /templates
        """
        uri = self.client.base_url + "/templates"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                resps = []
                for elem in resp.json():
                    resps.append(Template(elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)
