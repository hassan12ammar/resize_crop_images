import os
import pathlib
from typing import Tuple, Union
from PIL import Image, ImageOps
import tkinter.messagebox as messagebox

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()

def resize_crop_img(img:Image.Image, width:int, 
                        height:Union[int, None]) -> Union[Tuple[Image.Image, Image.Image], 
                                                            Tuple[Image.Image, None]]:
    """
    resize image based on an input width, 
    crop the image based on an input height if width passed,
    return resized image and the croped
    """
    ratio = img.size[1] / width
    resize_height = int(img.size[0] / ratio)
    resized_img = img.resize((resize_height, width))

    if height:
        resized_height = resized_img.size[1]   # width, height
        croped_img = ImageOps.crop(resized_img,(0, 0, 0, resized_height - height))  #left, top, right, bottom
        return resized_img, croped_img
    else:
        return resized_img, None

def main(input_path:str, resize_width:int, crop_height:int):
    """
    
    """
    if not input_path:
        input_path = os.path.join(CURRENT_PATH, "input")
        messagebox.showinfo("  ","\n   No path was entered I'm using input folder     ")

    out_path = os.path.join(CURRENT_PATH, "output")
    print("OutPut Path : ", out_path)
    files = os.listdir(input_path)
    img_extension = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
    for file in files:
        if file.lower().endswith(img_extension):
            print(file)
            img = Image.open(os.path.join(input_path, file))
            print('Original Dimensions : ',img.size)
            resized, croped = resize_crop_img(img, resize_width,crop_height)
            resized.save(fp = os.path.join(out_path, f"{resized.size[0]}*{resized.size[1]}_resized_{file}") )
            print('Resized Dimensions : ',resized.size)

            if croped != None:
                print('Croped Dimensions : ',croped.size)
                croped.save(os.path.join(out_path, f"{croped.size[0]}*{croped.size[1]}_croped_{file}"))

    messagebox.showinfo("  ","\n   Done!     ")
