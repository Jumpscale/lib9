from js9 import j




class UnhandledAPIError(Exception, ):
    """ UnhandledAPIError is exception when the API response doesnt have handler.

    It usually happens when the client receive status code
    that is not exist in the raml file.

    Args:
        response(obj): python requests object
        message: error message
    """

    def __init__(self, response, code, message):
        pass
        self.response = response
        self.code = code
        self.message = message
