# *-*-*-*-*-*-* -------- Creating a Dropdown Menu -------- *-*-*-*-*-*-*
# ----------------------------------------------------------------------

import tkinter as tk

window = tk.Tk()
window.geometry("800x600")
window.title("Animals")

label = tk.Label(window, text="Animals", bg="Yellow")
label.pack()

variable = tk.StringVar(window)
variable.set("Parrot")
w = tk.OptionMenu(window, variable, "Hamster", "Finch", "Whale", "Tiger")
w.pack()

window.mainloop()
