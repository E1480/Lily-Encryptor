"""
Encrypter Module
================
This module provides functionality for encrypting and decrypting files and folders using the Fernet symmetric encryption.
Functions:
----------
- init(): Initializes the encryption key and Fernet object.
- encrypt(file: str): Encrypts a given file asynchronously.
- decrypt(file: str): Decrypts a given file asynchronously.
- folderEncrypt(folder: str): Encrypts all files in a given folder asynchronously.
- __key__(): Returns the encryption key.
- __generateKey__(): Generates a new encryption key and saves it to a file.
- __change_key__(newKeyLocation: str): Changes the location of the key file and reinitializes the encryption setup.
Attributes:
-----------
- __home__: The path to the key file.
- key: The encryption key.
- fern: The Fernet object used for encryption and decryption.
Who needs docs?
"""
import os
from . import _configPath
from cryptography.fernet import Fernet
from os import listdir
from os.path import isfile


__home__ = _configPath.get()

key = None
fern = None

def init():
    global key
    global fern
    try:
        try:
            with open(__home__, 'x'):
                __generateKey__()
        except:
            with open(__home__, 'rb') as key:
                key = key.read()
                fern = Fernet(key)
    except Exception as e:
        pass

async def encrypt(file:str):
    try:
        with open(file, 'rb') as enFile:
            encrypted = fern.encrypt(enFile.read())
            with open(file, 'wb') as encrypt:
                encrypt.write(encrypted)

        original = file
        os.rename(original, original+'.muguet')

    except Exception as e:
        print(f'Error {e}')
        exit()



async def decrypt(file:str):
    try:
        with open(file, 'rb') as enFile:
            decrypted = fern.decrypt(enFile.read())
            with open(file, 'wb') as decrypt:
                decrypt.write(decrypted)

        original = file
        os.rename(original, original.replace('.muguet', ''))

    except Exception as e:
        print(f'Error {e}')
        exit()


async def folderEncrypt(folder:str):
    try:

        for file in listdir(folder):
            if isfile:
                await encrypt(file)
                print(file)


    except Exception as e:
        print(f'Error {e}')
        exit()

def __key__():
    try:
        with open(__home__, 'rb') as file:
            return file.read()
    except:
        return "Error"


def __generateKey__():
    global key
    global fern
    try:
        with open(__home__+'key', 'wb') as keyFile:
            key = Fernet.generate_key()
            fern = Fernet(key)
            keyFile.write(key)

    except Exception as e:
        print(f'Error {e}')
        exit()

def __change_key__(newKeyLocation:str):
    global __home__
    __home__ = newKeyLocation
    init()
