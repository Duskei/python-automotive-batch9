# System Configuration
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"
MAX_ATTEMPTS = 3

def login_manager(func):
    # This dictionary tracks the state (attempts and lock status)
    stats = {"attempts": 0, "is_locked": False}

    def loggedin():
        if stats["is_locked"]:
            print("\n[!] Account is temporarily locked. Please contact support.")
            return

        # Call the input function and get the result (True or False)
        success = func()

        if success:
            print("\n[+] Login Successful! Welcome back.")
            stats["attempts"] = 0 # Reset on success
        else:
            stats["attempts"] += 1
            remaining = MAX_ATTEMPTS - stats["attempts"]
            
            if stats["attempts"] >= MAX_ATTEMPTS:
                stats["is_locked"] = True
                print("\n[!] Too many failed attempts. Account locked.")
            else:
                print(f"\n[-] Invalid credentials. {remaining} attempts left.")
                # Recursively call wrapper to allow retry
                loggedin()

    return loggedin

@login_manager
def login_attempt():
    print("\n--- Secure Login System ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    # Validation logic
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return True
    return False

# Start the system
login_attempt()