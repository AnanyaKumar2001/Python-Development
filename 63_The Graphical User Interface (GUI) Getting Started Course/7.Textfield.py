# *-*-*-*-*-*-* -------- Creating a Textfield -------- *-*-*-*-*-*-*
# ------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox


def button_pressed():
    tk.messagebox.showinfo("Info", user_input.get())


window = tk.Tk()
window.geometry("500x300")

label = tk.Label(window, text="Welcome to my App", bg="Lawngreen")
label.pack()

user_input = tk.StringVar(window)
field = tk.Entry(window, textvariable=user_input)
field.pack()

button = tk.Button(window, text="Press",
                   command=button_pressed, bg="Lightblue")
button.pack()

window.mainloop()
