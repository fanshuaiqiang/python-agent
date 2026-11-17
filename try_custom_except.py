class MyError(Exception):
    """Custom exception class for demonstration purposes."""
    def __init__(self, message):
        # super().__init__(message)
        self.message = message

    def __str__(self):
        return f"MyError: {self.message}"



x = 10
if x > 5:
    raise MyError(f"x should not be greater than {x}")