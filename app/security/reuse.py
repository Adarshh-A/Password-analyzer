import hashlib

FILE = "data/passwords.db"

def _hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_reused(password):
    try:
        with open(FILE, "r") as f:
            return _hash(password) in f.read()
    except FileNotFoundError:
        return False

def save(password):
    with open(FILE, "a") as f:
        f.write(_hash(password) + "\n")
