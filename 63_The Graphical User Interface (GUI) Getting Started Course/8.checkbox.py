# *-*-*-*-*-*-* -------- Creating Checkboxes -------- *-*-*-*-*-*-*
# -----------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox


def button_pressed():
    if check_1_var.get() == 1 and check_2_var.get() == 1:
        tk.messagebox.showinfo(
            "Info", f"My name is {user_input.get()} and I love music and books")
    elif check_1_var.get() == 1:
        tk.messagebox.showinfo(
            "Info", f"My name is {user_input.get()} and I love music")
    elif check_2_var.get() == 1:
        tk.messagebox.showinfo(
            "Info", f"My name is {user_input.get()} and I love books")
    else:
        tk.messagebox.showinfo("Info", f"My name is {user_input.get()}")


window = tk.Tk()
window.geometry("350x350")
label = tk.Label(window, text="Select an Option", bg="Lawngreen")
label.pack()

check_1_var = tk.IntVar(window)
check_1 = tk.Checkbutton(window,
                         text="Music",
                         variable=check_1_var,
                         onvalue=1,
                         offvalue=0,
                         height=5,
                         width=20)
check_1.pack()


check_2_var = tk.IntVar(window)
check_2 = tk.Checkbutton(window,
                         text="Books",
                         variable=check_2_var,
                         onvalue=1,
                         offvalue=0,
                         height=5,
                         width=20)
check_2.pack()

user_input = tk.StringVar(window)
field = tk.Entry(window, textvariable=user_input)
field.pack()

button = tk.Button(window, text="Press",
                   command=button_pressed, bg="Lightblue")
button.pack()

window.mainloop()
