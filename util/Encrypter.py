import os
import asyncio
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
        with open(__home__, 'x'):
            __generateKey__()
    except:
        with open(__home__, 'rb') as key:
            key = key.read()
            fern = Fernet(key)

    
async def encrypt(file:str):
    try:
        with open(file, 'rb') as enFile:
            encrypted = fern.encrypt(enFile.read())
            with open(file, 'wb') as encrypt:
                encrypt.write(encrypted)
        
        original = file
        os.rename(original, original+'.muguet')

    except:
        pass


async def decrypt(file:str):
    try:
        with open(file, 'rb') as enFile:
            decrypted = fern.decrypt(enFile.read())
            with open(file, 'wb') as decrypt:
                decrypt.write(decrypted)

        original = file
        os.rename(original, original.replace('.muguet', ''))

    except:
        pass


async def folderEncrypt(folder:str):
    try:

        for file in listdir(folder):
            if isfile:
                await encrypt(file)
                print(file)


    except:
        pass

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
    except:
        pass

def __change_key__(newKeyLocation:str):
    global __home__
    __home__ = newKeyLocation
    init()

def __update__():
    pass