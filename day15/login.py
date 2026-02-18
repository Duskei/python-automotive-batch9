import hashlib
import time

# -----------------------------
# Simulated stored user data
# -----------------------------
stored_username = "admin"

# Hashing the password (simulating database storage)
stored_password_hash = hashlib.sha256("secure@123".encode()).hexdigest()

MAX_ATTEMPTS = 3
attempts = 0
lock_time = 10  # seconds (temporary lock)


def hash_password(password):
    """Converts plain password to hashed form"""
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate(username, password):
    """Validates user credentials"""
    return (
        username == stored_username and
        hash_password(password) == stored_password_hash
    )


# -----------------------------
# Login Logic
# -----------------------------
while attempts < MAX_ATTEMPTS:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if authenticate(username, password):
        print("Login successful. Welcome to the application.")
        break
    else:
        attempts += 1
        print(f"Invalid credentials. Attempts left: {MAX_ATTEMPTS - attempts}")

    if attempts == MAX_ATTEMPTS:
        print("Account locked temporarily due to multiple failed attempts.")
        print(f"Please wait {lock_time} seconds before trying again.")
        time.sleep(lock_time)
        attempts = 0   # reset attempts after lock period