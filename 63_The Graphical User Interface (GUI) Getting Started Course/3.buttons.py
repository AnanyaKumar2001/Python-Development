# *-*-*-*-*-*-* -------- Creating a Button -------- *-*-*-*-*-*-*
# ---------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox

window = tk.Tk()


def button_pressed():
    tk.messagebox.showinfo("Notice", "The Button was clicked")


# button = tk.Button(window, text="Click Me", command=button_pressed)

button = tk.Button(window,
                   text="Press",
                   command=button_pressed,
                   padx=10,
                   pady=12,
                   activebackground="Orange",
                   activeforeground="blue",
                   height=2,
                   width=7)

button.pack()

window.mainloop()
