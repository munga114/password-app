from Credentials import Credentials
import pyperclip as cb


class User(Credentials):
    
    def __init__(self):
        super().__init__()
        self.username = None
        self.password = None
        self.token = None

    def new_user(self, username, password):
        self.username = username
        self.password = password
        self.token = self.generate_token
        print(f"Welcome {username}, An account has been created for you, you can use the following token for "
              f"authentication.\n Your access token is {self.token} ")
        return {'username': username, 'password': password}

    def get_account_details(self, account_name):