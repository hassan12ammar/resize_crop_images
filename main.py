# libraries
import os
import tkinter as tk
import tkinterdnd2 as tkt
# local files
from utlize import CURRENT_PATH, main

def drop(event):
    path_var.set(event.data)

def click():
    path = path_var.get().strip('"\'')
    width = None
    height = None

    if e_width.get():
        width = int(e_width.get())
    if e_height.get():
        height = int(e_height.get())

    print(path, width, height)
    main(path, width, height)

root = tkt.Tk()
root.title('resize and crop images')
root.geometry('500x300')
root.config(bg='#d35400')  # fcba03 

path_var = tk.StringVar()
tk.Label(root, text='Path of the Folder: ',fg="black", bg='#d35400').pack(anchor=tk.NW)
e_box = tk.Entry(root, textvar=path_var, width=80)
e_box.pack(fill=tk.X, padx=10)
e_box.drop_target_register(tkt.DND_FILES)
e_box.dnd_bind('<<Drop>>', drop)

tk.Label(root, text='resize width: ',fg="black", bg='#d35400').pack()
e_width = tk.Entry(root, width=40)
e_width.pack()

tk.Label(root, text='crop height: ',fg="black", bg='#d35400').pack()
e_height = tk.Entry(root, width=40)
e_height.pack()

bt = tk.Button(root,text = 'Enter', command = click, width = 8)
bt.pack()

lframe = tk.LabelFrame(root, text='Instructions', bg='#090909')
tk.Label(
    lframe, 
    bg='#090909',
    text='Drag and drop the folder \nof your input in the path field.\nenter integer number for the width field.\
        \nenter integer number for the height field.\n if you want to crop the image after resize it.\
        \n You will have the output in out folder.',
    ).pack(fill=tk.BOTH,side="top")
lframe.pack(fill=tk.BOTH,expand=True, padx=10, pady=10)


if __name__ == "__main__":
    if not os.path.exists(os.path.join(CURRENT_PATH, 'out')):
        os.makedirs(os.path.join(CURRENT_PATH, 'out'))
    if not os.path.exists(os.path.join(CURRENT_PATH, 'input')):
        os.makedirs(os.path.join(CURRENT_PATH, 'input'))
    root.mainloop()

