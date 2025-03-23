# Copyright (c) 2025 E1480
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


import tkinter as tk
from tkinter import Button, Entry, Frame, LabelFrame, filedialog
import os
import shutil
import time
from . import hash

template = """# Copyright (c) 2025 E1480
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
from util import hash
from cryptography.fernet import Fernet
import os

hashed = {hash}
offset = -9


DIR = filter(os.path.isfile, os.listdir('./'))



def removeSelf():
    os.remove('./util/hash.py')
    os.rmdir('./util')
    os.remove('./lily.py')
    exit()

    
def decrypt():
    STATUS = None
    try:
        for i in DIR:
            if i.endswith('.muguet'):
                with open('./'+i, 'rb') as enFile:
                    decrypted = Fernet(getKey()).decrypt(enFile.read())
                    with open('./'+i, 'wb') as decrypt:
                        decrypt.write(decrypted)

                original = './'+i
                os.rename(original, original.replace('.muguet', ''))
        STATUS = True
    except:
        STATUS = False

    
    if STATUS:
        messagebox.showinfo('Lily Password', "Success.")
        removeSelf()
    

def getKey() -> bytes:
    for i in DIR:
        if i == 'key':
            with open('./'+i, 'rb') as file:
                return file.read()
        



def init(screenWidth="260x50", screenTitle="Lily"):

    def check():
        pasw = passwordEntry.get()
        hashedPass = hash.Hash().make(pasw, 'utf-8', 'bytes')
        hashedPass = hashedPass.rstrip(hashedPass[-9:])
        if hashedPass != hashed:
            messagebox.showerror('Lily Password', "Wrong password.")
        else:
            decrypt()

    root = tk.Tk()
    root.title(screenTitle)
    root.geometry(screenWidth)
    root.resizable(False, False)

    passwordLbl = Label(text='Enter Password:')
    passwordEntry = Entry()
    passwordSubmit = Button(text='Submit', command=check)

    passwordLbl.grid(row=0, column=0)
    passwordEntry.grid(row=0, column=1)
    passwordSubmit.grid(row=0, column=2)


    root.mainloop()



if __name__ == "__main__":
    init()"""

templateWKey = """# Copyright (c) 2025 E1480
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
from util import hash
from cryptography.fernet import Fernet
import os

hashed = {hash}
key = {key}
offset = -9


DIR = filter(os.path.isfile, os.listdir('./'))



def removeSelf():
    os.remove('./util/hash.py')
    os.rmdir('./util')
    os.remove('./lily.py')
    exit()

    
def decrypt():
    STATUS = None
    try:
        for i in DIR:
            if i.endswith('.muguet'):
                with open('./'+i, 'rb') as enFile:
                    decrypted = Fernet(key).decrypt(enFile.read())
                    with open('./'+i, 'wb') as decrypt:
                        decrypt.write(decrypted)

                original = './'+i
                os.rename(original, original.replace('.muguet', ''))
        STATUS = True
    except:
        STATUS = False

    
    if STATUS:
        messagebox.showinfo('Lily Password', "Success.")
        removeSelf()
    


def init(screenWidth="260x50", screenTitle="Lily"):

    def check():
        pasw = passwordEntry.get()
        hashedPass = hash.Hash().make(pasw, 'utf-8', 'bytes')
        hashedPass = hashedPass.rstrip(hashedPass[-9:])
        if hashedPass != hashed:
            messagebox.showerror('Lily Password', "Wrong password.")
        else:
            decrypt()

    root = tk.Tk()
    root.title(screenTitle)
    root.geometry(screenWidth)
    root.resizable(False, False)

    passwordLbl = Label(text='Enter Password:')
    passwordEntry = Entry()
    passwordSubmit = Button(text='Submit', command=check)

    passwordLbl.grid(row=0, column=0)
    passwordEntry.grid(row=0, column=1)
    passwordSubmit.grid(row=0, column=2)


    root.mainloop()



if __name__ == "__main__":
    init()
"""

def init(screenWidth="500x100", screenTitle="Lily"):
    def openFile():
        global KEY
        keyFile = filedialog.askopenfile()
        key.config(state=tk.NORMAL)
        key.insert(tk.END, keyFile.name)
        key.config(state=tk.DISABLED)
        try:
            with open(key.get(), 'rb') as FILE:
                KEY = FILE.read()
        except Exception as e:
            print(e)


    def Gen():
        try:
            if password.index("end") == 0:
                pass
            if len(password.get()) < 10:
                print('password mst be 10 char long')
            if key.get() != '':
                makefile()

                output = hash.Hash().make(password.get(), 'utf-8', 'bytes')
                secret = output.rstrip(output[-9:])
                try:
                    with open('./bin/lily.py', 'w') as file:
                        file.write(templateWKey.format(hash = secret, key=KEY))
                        time.sleep(1)
                        shutil.copy('./util/hash.py', './bin/util')
                except:
                    pass
            else:
                makefile()

                output = hash.Hash().make(password.get(), 'utf-8', 'bytes')
                secret = output.rstrip(output[-9:])
                try:
                    with open('./bin/lily.py', 'w') as file:
                        file.write(template.format(hash=secret))
                        time.sleep(1)
                        shutil.copy('./util/hash.py', './bin/util')
                except:
                    pass

        except OSError as e:
            print(e)

    def makefile():
        if os.path.exists('./bin'):
            shutil.rmtree('./bin')
        time.sleep(1)
        if not os.path.exists('./bin'):
            os.makedirs('./bin')
            os.makedirs('./bin/util')


    root = tk.Tk()
    root.title(screenTitle)
    root.geometry(screenWidth)

    passlabelframe = LabelFrame(root, text="Password", padx=10, pady=10)
    passlabelframe.grid(row=0, column=0, padx=10, pady=10)

    passwframe = Frame(passlabelframe)
    passwframe.grid(row=0, column=0, padx=10, pady=10)

    password = Entry(passwframe)
    password.grid(row=0, column=1)

#   Key 

    keylabelframe = LabelFrame(root, text="Key", padx=10, pady=10)
    keylabelframe.grid(row=0, column=1, padx=10, pady=10)

    keyframe = Frame(keylabelframe)
    keyframe.grid(row=0, column=1, padx=10, pady=10)

    key = Entry(keyframe, state='disabled')
    key.grid(row=0, column=0)
    Button(keyframe, text='...', command=openFile).grid(row=0, column=1)

    Button(root, text='Generate', command=Gen).grid(row=0, column=2)


    root.mainloop()