# Copyright (c) 2025 E1480
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import tkinter as tk
from tkinter import Entry, Label, Button, messagebox


hash = None

def init(screenWidth="260x50", screenTitle="Lily"):


    def check():

        messagebox.showerror('Lily Password', "Wrong password.")

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