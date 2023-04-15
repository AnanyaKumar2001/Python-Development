# *-*-*-*-*-*-* -------- Addding Background Images -------- *-*-*-*-*-*-*
# -----------------------------------------------------------------------

# pip install pillow

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("550x450")

image = Image.open(r"C:\image.jpg")
image = image.resize((550, 450), Image.ANTIALIAS)

test = ImageTk.PhotoImage(image)

label = tk.Label(image=test)
label.place(x=0, y=0)

window.mainloop()
