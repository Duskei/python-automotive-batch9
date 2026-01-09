# test_auth.py
import pytest
from auth import LoginSystem, MAX_ATTEMPTS

@pytest.fixture
def system():
    """Provides a fresh instance of LoginSystem for each test."""
    return LoginSystem()

def test_successful_login(system):
    assert system.login("admin", "password123") == "SUCCESS"
    assert system.attempts == 0

def test_failed_login_decrements_attempts(system):
    result = system.login("admin", "wrong_pass")
    assert result == "FAILED"
    assert system.attempts == 1

def test_account_locking_after_max_attempts(system):
    # Simulate failed attempts up to the limit
    for i in range(MAX_ATTEMPTS - 1):
        system.login("admin", "bad_pass")
    
    # The final failing attempt
    last_result = system.login("admin", "bad_pass")
    
    assert last_result == "LOCKED"
    assert system.is_locked is True

def test_cannot_login_while_locked(system):
    system.is_locked = True
    assert system.login("admin", "password123") == "LOCKED"

@pytest.mark.parametrize("u, p, expected", [
    ("wrong", "password123", "FAILED"),
    ("admin", "wrong", "FAILED"),
    ("", "", "FAILED"),
])
def test_various_invalid_credentials(system, u, p, expected):
    assert system.login(u, p) == expected