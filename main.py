from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
import subprocess
from tkinter import filedialog

root = Tk()
root.title("Python IDE")
root.geometry("800x700")
toolbar = Menu(root)


def Exit():
    root.destroy()

def save_file():
    code = inputCodefield.get("1.0", "end")
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)    

def run_cmd():
    code_content = inputCodefield.get("1.0", tk.END)
    with open("yourprogram.py", "w", buffering=1024) as file:
        file.write(code_content)
    subprocess.Popen("cmd /K python yourprogram.py", creationflags=subprocess.CREATE_NEW_CONSOLE)
        
def paste_one():
    text = root.clipboard_get()
    inputCodefield.insert(tk.END, text)       
    
def clear_field():
    inputCodefield.delete("1.0", tk.END)

def open_py_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    with open(file_path, "r", encoding="utf-8") as file:
        py_content = file.read()
        inputCodefield.insert(tk.END, py_content)

def open_txt_file():
    file_path = filedialog.askopenfilename(filetypes=[("TEXT files", "*.txt")])
    with open(file_path, "r", encoding="utf-8") as file:
        txt_content = file.read()
        inputCodefield.insert(tk.END, txt_content)


  
inputCodefield = scrolledtext.ScrolledText(root, width=300, height=500)
inputCodefield.pack()





file = Menu(root, tearoff=0)
toolbar.add_cascade(label="File", menu=file)
file.add_command(label="save", command=save_file)
file.add_command(label="save as", command=None)
file.add_command(label="exit", command=Exit)
file.add_command(label="import txt", command=open_txt_file)
file.add_command(label="import py", command=open_py_file)

edit = Menu(root, tearoff=0)
toolbar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="clear all", command=clear_field)
edit.add_command(label="paste", command=paste_one)
edit.add_command(label="copy")



functions = Menu(root, tearoff=0)
toolbar.add_radiobutton(label="run code", command=run_cmd)



root.config(menu=toolbar)
root.mainloop()
