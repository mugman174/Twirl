class TwirlException(Exception):
    pass
class IncorrectArgumentFormatError(TwirlException):
    def __init__(self, *args):
        print(f"Error: {args}")