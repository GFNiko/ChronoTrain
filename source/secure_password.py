import base64
import hashlib

import bcrypt


"""
Password hashing and encryption algorithms, using bcrypt, sha-256 and utf-8 encoding
"""


SALT = 12
ENCODE = "utf-8"


def gen_password_hash(password: str) -> str:
    """ Encrypts password """
    password = password.encode(ENCODE)
    password = base64.b64encode(hashlib.sha256(password).digest())
    hashed = bcrypt.hashpw(
        password,
        bcrypt.gensalt(SALT)
    )
    return hashed.decode()


def check_password(password: str, hash: str) -> bool:
    """ checks given password and encryption """
    password = password.encode(ENCODE)
    password = base64.b64encode(hashlib.sha256(password).digest())
    hash = hash.encode(ENCODE)
    return bcrypt.checkpw(password, hash)
