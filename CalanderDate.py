

class UserCalanderDate:
    """Represents API information to be used for calls from the user and stores that information
    for easier use."""

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'Year: {self.year}, Month: {self.month}, Day: {self.day}'

