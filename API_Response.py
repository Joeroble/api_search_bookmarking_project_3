"""API Response handles the data returned or not from an API, it stores the data returned.  It also will store information related to a user_error, or a connection
error if needed."""


class API_Response:
    def __init__(self, data = None, user_error = None, connection_error = None):
        self.data = data
        self.user_error = user_error
        self.connection_error = connection_error


 
    def __str__(self):
        return f'Data: {self.data}, User error: {self.user_error}, Connection error: {self.connection_error}'