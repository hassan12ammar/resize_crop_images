import tkinter as tk
import tkinterdnd2 as tkt
import tkinter.messagebox as messagebox
import os
import pathlib
from PIL import Image, ImageOps

def resize_crop_img(img,width_input,height_input):
    ratio = img.size[1] / width_input
    height = int(img.size[0] / ratio)
    resized_img = img.resize((height,width_input))
    if height_input != None:
        resized_height = resized_img.size[1]   # width, height
        croped_img = ImageOps.crop(resized_img,(0, 0, 0, resized_height-height_input))  #left, top, right, bottom
        return resized_img, croped_img
    else:
        return resized_img, None

def main_(input_path,resize_width,crop_height):
    if input_path == "":
        input_path = f"{current_path}/input"
        messagebox.showinfo("  ","\n   No path was entered I'm using input folder     ")
    out_path = f"{current_path}/out"
    os.chdir(f"{input_path}")
    files = os.listdir(input_path)
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            # tkinter.messagebox.showinfo("file",file)
            print(file)
            img=Image.open(f"{input_path}/{file}")
            # tkinter.messagebox.showinfo('Original Dimensions : ',img.shape)
            print('Original Dimensions : ',img.size)
            resized, croped = resize_crop_img(img,resize_width,crop_height)
            resized.save(f'{out_path}/{resized.size[0]}*{resized.size[1]}_resized_{file}') 
            # tkinter.messagebox.showinfo('Resized Dimensions : ',resized.shape)
            print('Resized Dimensions : ',resized.size)
            if croped != None:
                print('Croped Dimensions : ',croped.size)
                croped.save(f'{out_path}/{croped.size[0]}*{croped.size[1]}_croped_{file}')
    messagebox.showinfo("  ","\n   Done!     ")


def drop(event):
    var.set(event.data)

def click():
    path = var.get()
    input_width = None
    input_height = None
    if e_width.get():
        input_width = int(e_width.get())
    if e_height.get():
        input_height = int(e_height.get())
    print(path,input_width,input_height)
    main_(path,input_width,input_height)

ws = tkt.Tk()
ws.title('resize and crop images')
ws.geometry('500x300')
ws.config(bg='#d35400')  # fcba03 

var = tk.StringVar()
tk.Label(ws, text='Path of the Folder: ',fg="black", bg='#d35400').pack(anchor=tk.NW)
e_box = tk.Entry(ws, textvar=var, width=80)
e_box.pack(fill=tk.X, padx=10)
e_box.drop_target_register(tkt.DND_FILES)
e_box.dnd_bind('<<Drop>>', drop)

tk.Label(ws, text='resize width: ',fg="black", bg='#d35400').pack()
e_width = tk.Entry(ws, width=40)
e_width.pack()

tk.Label(ws, text='crop height: ',fg="black", bg='#d35400').pack()
e_height = tk.Entry(ws, width=40)
e_height.pack()

bt=tk.Button(ws,text = 'Enter', command = click, width = 8)
bt.pack()

lframe = tk.LabelFrame(ws, text='Instructions', bg='#090909')
tk.Label(
    lframe, 
    bg='#090909',
    text='Drag and drop the folder \nof your input in the path field.\nenter integer number for the width field.\nenter integer number for the height field.\n if you want to crop the image after resize it.\n You will have the output in out folder.',
    ).pack(fill=tk.BOTH,side="top")
lframe.pack(fill=tk.BOTH,expand=True, padx=10, pady=10)


current_path = pathlib.Path(__file__).parent.resolve()
if __name__ == "__main__":
    if not os.path.exists(f'{current_path}/out'):
        os.makedirs(f'{current_path}/out')
    if not os.path.exists(f'{current_path}/input'):
        os.makedirs(f'{current_path}/input')
    ws.mainloop()
