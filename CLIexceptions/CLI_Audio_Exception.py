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
