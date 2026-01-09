# auth.py
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"
MAX_ATTEMPTS = 3

class LoginSystem:
    def __init__(self):
        self.attempts = 0
        self.is_locked = False

    def login(self, username, password):
        if self.is_locked:
            return "LOCKED"

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            self.attempts = 0
            return "SUCCESS"
        else:
            self.attempts += 1
            if self.attempts >= MAX_ATTEMPTS:
                self.is_locked = True
                return "LOCKED"
            return "FAILED"