from string import ascii_letters, digits, punctuation
from secrets import choice, token_hex


class Credentials:

    def __init__(self):
        self.accounts = []

    def generate_password(self, password_length=None):
        alphabets = ascii_letters + digits + punctuation
        if password_length is None:
            password_length = int(input('Specify the length of password you wish to generate (positive int): '))
        else:
            password_length = int(password_length)
        while True:
            password = ''.join(choice(alphabets) for i in range(password_length))
            try:
                accept = int(
                    input(f"Generated password is {password}.\n Reply with 1 to accept or 2 to generate another "
                          f"password\n"))
                if accept == 1:
                    return password
                else:
                    continue
            except ValueError:
                return f"You've provided an invalid input."