# -*- coding: utf-8 -*-

# Python program to convert 
# JSON file to CSV 
  
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import json
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'ivory4', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='JSON to CSV Tool', bg = 'ivory4')
label1.config(font=('ubuntu', 20))
canvas1.create_window(150, 60, window=label1)

def getJSON ():
    global df
    import_file_path = filedialog.askopenfilename(initialdir = '/home/')
    with open(import_file_path, 'r') as f:
        data = json.load(f)
        df = pd.DataFrame([data])
    
browseButton_JSON = tk.Button(text="      Import metaData.json     ", command=getJSON, bg='sea green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_JSON)

def convertToCSV ():
    global df
    export_file_path = filedialog.asksaveasfilename(initialdir = '/home/', defaultextension = '.csv')
    df.to_csv (export_file_path, index = None, header=True)

saveAsButton_CSV = tk.Button(text='Convert to metaData.csv', command=convertToCSV, bg='orange2', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_CSV)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()
