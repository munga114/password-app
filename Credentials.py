from string import ascii_letters, digits, punctuation
from secrets import choice, token_hex


class Credentials:

    def __init__(self):
        self.accounts = []

    def generate_password(self, password_length=None):