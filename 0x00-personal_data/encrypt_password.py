#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Implement a hash_password function that expects one string
    argument name password and returns a salted, hashed
    password, which is a byte string.
    '''
    pass_encoded = password.encode()
    # Hash a password for the first time, with a randomly-generated salt
    pass_hashed = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return pass_hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Implement an is_valid function that expects 2 arguments and
    returns a boolean.
    '''
    valid = False
    pass_encoded = password.encode()
    if bcrypt.checkpw(pass_encoded, hashed_password):
        valid = True
    return valid
