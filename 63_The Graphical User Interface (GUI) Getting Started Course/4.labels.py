# *-*-*-*-*-*-* -------- Creating a Label -------- *-*-*-*-*-*-*
# --------------------------------------------------------------

import tkinter as tk

window = tk.Tk()

window.geometry("250x250")

# label = tk.Label(window, text="Hello World", bg="Orange")

label = tk.Label(window, text="Hello World", bg="Orange", padx=8, pady=10)

label.pack()

window.mainloop()
