from tkinter import *
import time
import os
root = Tk()
from PIL import Image
 

imageObject = Image.open("./mygif.gif")
print(imageObject.n_frames)
frameCnt = imageObject.n_frames
frames = [PhotoImage(file='mygif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
    
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()