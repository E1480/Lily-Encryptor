# Copyright (c) 2025 E1480
"""
hash.py
This module provides a Hash class for generating SHA-256 hashes and PBKDF2-HMAC hashes.
Classes:
    Hash: A class for creating SHA-256 and PBKDF2-HMAC hashes.
Usage example:
    hash_instance = Hash()
    sha256_hash = hash_instance.make("example text")
    pbkdf2_hash = hash_instance.makePbkdf2_hmac("password", b'salt', 1, 100000)
License:
    This software is released under the MIT License.
    https://opensource.org/licenses/MIT
"""

# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import hashlib
from typing import Literal

class Hash:
    def __init__(self):
        self.lib = hashlib.sha256()

    def make(self, text:str, strEncoding:str="utf-8", type:Literal['bytes', 'hex'] = 'bytes') -> str:
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
