
import os
import hashlib
from typing import Literal

"""
# hash.py
This module provides a Hash class for creating hash digests using SHA-256 and PBKDF2-HMAC.

Classes:
    Hash: A class for generating hash digests.

Usage:
    hash_instance = Hash()
    digest = hash_instance.make("example text", "utf-8", "hex")
    pbkdf2_digest = hash_instance.makePbkdf2_hmac("password", b'salt', 2, 100000)
    salt = hash_instance.__salt__()

License:
    This software is released under the MIT License.
    https://opensource.org/licenses/MIT
"""

class Hash:
    """
    A class used to generate hash digests using SHA-256 and PBKDF2-HMAC.

    Methods:
        __init__(): Initializes the Hash object with a SHA-256 hash library.
        make(text: str, strEncoding: str, type: Literal['bytes', 'hex'] = 'bytes') -> str:
            Generates a hash digest of the given text.
        makePbkdf2_hmac(password: str, salt: bytes, offset: int, itter: int) -> str:
            Generates a PBKDF2-HMAC hash digest of the given password.
        __salt__() -> bytes:
            Generates a random salt.
    """

    def __init__(self):
        """
        Initializes the Hash object with a SHA-256 hash library.
        """
        self.lib = hashlib.sha256()

    def make(self, text: str, strEncoding: str, type: Literal['bytes', 'hex'] = 'bytes') -> str:
        """
        Generates a hash digest of the given text.

        Args:
            text (str): The text to hash.
            strEncoding (str): The encoding of the text.
            type (Literal['bytes', 'hex']): The type of digest to return ('bytes' or 'hex').

        Returns:
            str: The hash digest in the specified format.
        """
        self.lib.update(bytes(text.encode(strEncoding)))
        try:
            if type == 'bytes':
                return self.lib.digest()
            elif type == 'hex':
                return self.lib.hexdigest()
        except Exception as e:
            print(f"Error digest: {e}")
            return "Error"

    def makePbkdf2_hmac(self, password: str, salt: bytes, offset: int, itter: int) -> str:
        """
        Generates a PBKDF2-HMAC hash digest of the given password.

        Args:
            password (str): The password to hash.
            salt (bytes): The salt to use in the hashing process.
            offset (int): The offset to multiply the salt.
            itter (int): The number of iterations for the hashing process.

        Returns:
            str: The PBKDF2-HMAC hash digest in hexadecimal format.
        """
        pasw = password.encode('utf-8')
        secret = hashlib.pbkdf2_hmac('sha256', bytes(pasw), salt * offset, itter)
        return secret.hex()

    def __salt__(self) -> bytes:
        """
        Generates a random salt.

        Returns:
            bytes: A random salt.
        """
        return os.urandom(16)

# Copyright (c) 2025 E1480
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


class Hash:
    def __init__(self):
        self.lib = hashlib.sha256()

    def make(self, text:str, strEncoding:str, type:Literal['bytes', 'hex'] = 'bytes') -> str:
        self.lib.update(bytes(text.encode(strEncoding)))
        try:
            if type == 'bytes':
                bytesDigest = self.lib.digest()
                return bytesDigest
            if type == 'hex':
                hexDigest = self.lib.hexdigest()
                return hexDigest
            
        except Exception as e:
            print(f"Error digest: {e}")
            return "Error"

    def makePbkdf2_hmac(self, passwrod:str, salt:bytes, offset:int, itter:int) -> str:
        pasw = passwrod.encode('utf-8')
        secret = hashlib.pbkdf2_hmac('sha256', bytes(pasw), salt * offset, itter )
        return secret.hex()


    def __salt__(self) -> bytes:
        return os.urandom(16)
