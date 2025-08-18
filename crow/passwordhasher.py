import base64
import hashlib


def compute_hash(password, salt):
    password = password.encode()
    salt = salt.encode()
    hashed = salt + password
    for i in range(1000):
        hashed = hashlib.sha512(hashed).digest()

    return salt + base64.b64encode(hashed)
