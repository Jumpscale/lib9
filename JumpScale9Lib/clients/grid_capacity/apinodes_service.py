# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.


class ApinodesService:
    def __init__(self, client):
        self.client = client

    def ListCapacity(self, headers=None, query_params=None, content_type="application/json"):
        """
        List all the nodes capacity
        It is method for GET /api/nodes
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/api/nodes"
        return self.client.get(uri, None, headers, query_params, content_type)

    def RegisterCapacity(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Register a node capacity
        It is method for POST /api/nodes
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/api/nodes"
        return self.client.post(uri, data, headers, query_params, content_type)
