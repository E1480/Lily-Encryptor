import tkinter as tk
from . import _configPath 
from . import Encrypter as en
from tkinter import Text, Menu, filedialog, Label
from typing import Literal
import asyncio
from os import listdir
from os.path import isfile

def init(screenWidth="400x500", screenTitle="Lily"):

    def log(value:str, type:Literal['Normal','Success','Error', 'Warn'] = 'Normal'):
        if type == 'Normal':
            log_text.config(state=tk.NORMAL)
            log_text.insert(tk.END, value + '\n')
            log_text.config(state=tk.DISABLED)
        if type == 'Success':
            log_text.config(state=tk.NORMAL)
            log_text.insert(tk.END, value + '\n', 'green')
            log_text.tag_config("green", foreground="white", background="green")
            log_text.config(state=tk.DISABLED)
        if type == 'Error':
            log_text.config(state=tk.NORMAL)
            log_text.insert(tk.END, value + '\n', 'red')
            log_text.tag_config("red", foreground="red")
            log_text.config(state=tk.DISABLED)
        if type == 'Warn':
            log_text.config(state=tk.NORMAL)
            log_text.insert(tk.END, value + '\n', 'black')
            log_text.tag_config("black", foreground="black", background="orange", )
            log_text.config(state=tk.DISABLED)


        log_text.see(tk.END)


    def encrypt():
        file = filedialog.askopenfilename()
        if file != '':
            print(file)
            try:
                log('Encrypting...')
                asyncio.run(en.encrypt(file))
                log('Success!!!', 'Success')
            except:
                log('Encryption Error: No Key.', 'Error')
        else:
            log("No file chosen.")

    def decrypt():
        file = filedialog.askopenfilename()
        if file != '':
            try:
                log('Decrypting...')
                asyncio.run(en.decrypt(file))
                log('Success!!!', 'Success')
            except:
                log('Decryption Error: No Key.', 'Error')
        else:
            log('No file chosen.')

    def folderEncrypt():
        folder = filedialog.askdirectory()

        try:
            for file in listdir(folder):
                log(f'Encrypting: {file}')
                fullFile = folder+'/'+file
                if isfile:
                    asyncio.run(en.encrypt(fullFile))
            log('Encryption Sucess!!', 'Success')

        except:
            log('Encryption Error: No Key.', 'Error')

    def folderDecrypt():
        folder = filedialog.askdirectory()
        try:
            for file in listdir(folder):
                log(f'Decrypting: {file}')
                fullFile = folder+'/'+file
                if isfile:
                    asyncio.run(en.decrypt(fullFile))
            log('Decryption Sucess!!', 'Success')
        except:
            log('Decryption Error: No Key.', 'Error')


    def key():
        log('Key bytes:')
        log(repr(en.__key__()), 'Success')
        log('DO NOT LOSE THIS', 'Warn')


    def fileKey():
        keyFile = filedialog.askdirectory()
        log('Opening key directory...')
        try:
            en.__change_key__(keyFile+'/key')
            log('Changed key Success!', 'Success\n')
            _configPath.update(keyFile+'/key')
            key()
        except Exception as e:
            log(f'Failed to open key folder: {e}')



    root = tk.Tk()
    root.title(screenTitle)
    root.geometry(screenWidth)
    
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Key', command=key)
    file_menu.add_command(label='Key Folder', command=fileKey)

    encrypt_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Encrypt', menu=encrypt_menu)
    encrypt_menu.add_command(label='File', command=encrypt)
    encrypt_menu.add_command(label='Folder', command=folderEncrypt)
    
    decrypt_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Decrypt', menu=decrypt_menu)
    decrypt_menu.add_command(label='File', command=decrypt)
    decrypt_menu.add_command(label='Folder', command=folderDecrypt)


    log_text = Text(root, state='disabled')
    log_text.pack()
    log('Log:\n')

    Label(text='Made By: E1480').pack()
    Label(text='For unknown reasons').pack()
    

    root.mainloop()