"""API Response handles the data returned or not from an API, it stores the data returned."""




class API_Response:
    def __init__(self, data, user_error, connection_error, status_description):
        self.data = data
        self.user_error = user_error
        self.connection_error = connection_error
        self.status_description = status_description

 
    def __str__(self):
        return f'Data: {self.data}, User error: {self.user_error}, Connection error: {self.connection_error}, Status description{self.status_description}'