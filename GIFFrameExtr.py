from PIL import Image as PILImage
import tgs
import os
from tkinter import filedialog
from tkinter import *

def FrameExtract():
    inputDir = folder_path.get()
    filesList = os.listdir(inputDir)
    for emoticon in filesList:
        fileName = emoticon[:-4]
        fileExt = emoticon[-4:]
        if fileExt == ".gif":
            inputGIF = PILImage.open(inputDir + "/" + fileName + fileExt)
            GIFlength = inputGIF.info["duration"]
            resizeRatio = (inputGIF.size[1] / inputGIF.size[0])

            if not os.path.exists(fileName):
                os.mkdir(fileName)

            for frame in range(GIFlength):
                try:
                    inputGIF.seek(frame)
                    inputGIF.save(fileName + "/" + fileName + '{:04d}'.format(frame) + ".png")
                except EOFError:
                    break
        else:
            next


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

mainWindow = Tk()
mainWindow.geometry('320x240')
folder_path = StringVar()
lbl1 = Label(master=mainWindow,textvariable=folder_path)
lbl1.grid(row=1, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=2, column=1)
button3 = Button(text="Run", command=FrameExtract)
button3.grid(row=2, column=2)

mainWindow.mainloop()

