from Credentials import Credentials
import pyperclip as cb


class User(Credentials):
    
    def __init__(self):
        super().__init__()
        self.username = None
        self.password = None
        self.token = None