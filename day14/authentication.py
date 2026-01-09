import hashlib
import time

class SecureLoginSystem:
    def __init__(self):
        # Simulated user database: username -> (hashed_password, is_locked, lock_until)
        self.users = {
            'user1': (self.hash_password('password123'), False, 0),
            'admin': (self.hash_password('adminpass'), False, 0)
        }
        self.max_attempts = 3
        self.lock_duration = 60  # seconds (1 minute for demo)

    def hash_password(self, password):
        """Hash password using SHA-256 for security."""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def validate_input(self, input_str):
        """Validate input: strip whitespace and check if not empty."""
        cleaned = input_str.strip()
        if not cleaned:
            raise ValueError("Input cannot be empty.")
        return cleaned

    def is_locked(self, username):
        """Check if account is locked and if lock has expired."""
        if username not in self.users:
            return False
        _, is_locked, lock_until = self.users[username]
        if is_locked and time.time() < lock_until:
            return True
        if is_locked:  # Unlock if time expired
            self.users[username] = (self.users[username][0], False, 0)
        return False

    def lock_account(self, username):
        """Lock the account temporarily."""
        if username in self.users:
            lock_until = time.time() + self.lock_duration
            self.users[username] = (self.users[username][0], True, lock_until)
            print(f"Account '{username}' locked for {self.lock_duration} seconds.")

    def login(self):
        """Main login logic with attempt counter and validation."""
        attempts = 0
        while attempts < self.max_attempts:
            try:
                username = self.validate_input(input("Enter username: "))
                if self.is_locked(username):
                    print("Account is temporarily locked. Try again later.")
                    return False

                password = self.validate_input(input("Enter password: "))
                hashed_pw = self.hash_password(password)

                if username in self.users and self.users[username][0] == hashed_pw:
                    print("Login successful!")
                    return True
                else:
                    attempts += 1
                    remaining = self.max_attempts - attempts
                    print(f"Invalid username or password. {remaining} attempts remaining.")
            except ValueError as e:
                print(f"Validation error: {e}")
                continue  # Don't count invalid input as an attempt

        # All attempts failed
        self.lock_account(username)
        print("Maximum attempts reached. Account locked.")
        return False

# Usage example
if __name__ == "__main__":
    system = SecureLoginSystem()
    system.login()