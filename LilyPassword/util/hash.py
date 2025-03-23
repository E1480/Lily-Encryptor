# Copyright (c) 2025 E1480
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import hashlib
from typing import Literal

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
