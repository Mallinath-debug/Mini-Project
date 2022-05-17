from tkinter import *
import tkinter

from PIL import ImageTk,Image     #for image
import os


def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter=counter+1

counter=1
root=Tk()

root.title('Wallpaper Viewer')           # for title on the window

root.geometry('250x400')                  #geometry of the app
 
root.config(background='black')            #for background color

files=os.listdir('wallpapers')
print(files)

img_array=[]
for file in files:
    img=Image.open(os.path.join('wallpapers',file))
    resize_img=img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resize_img))

img_label=Label(root,image=img_array[0])
img_label.pack(pady=(15,10))

next_btn=Button(root,text='Next',bg='white',fg='black',width=25,height=2,command=rotate_image)
next_btn.pack()






root.mainloop()            #to hold on the screen
