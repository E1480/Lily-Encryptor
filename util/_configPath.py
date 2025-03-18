# Copyright (c) 2025 E1480
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os

__home__ = os.path.abspath(os.path.dirname( __file__ )) + '\\paths.txt'

def update(newPath:str):
    try:
        with open(__home__, 'rw') as file:
            file.write(newPath)

    except:
        pass

def get():
    with open(__home__, 'r') as file:
        return file.read()