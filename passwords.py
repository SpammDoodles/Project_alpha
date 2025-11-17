import hashlib
import secrets

def hash_password(password: str) -> tuple[str, str]:
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return salt, hashed

def verify_password(password: str, salt: str, hashed: str) -> bool:
    return hashlib.sha256((salt + password).encode()).hexdigest() == hashed
