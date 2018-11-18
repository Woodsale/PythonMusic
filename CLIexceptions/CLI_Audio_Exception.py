#https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
#Parent class for exception handling. Used link above to learn how to throw exceptions
class CLI_Audio_Exception(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class CLI_Audio_File_Exception(CLI_Audio_Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class CLI_Audio_Screen_Size_Exception(CLI_Audio_Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
