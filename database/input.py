import tkinter as tk
from decimal import Decimal as dec, getcontext
import os
import pandas as pd
import random as rd

os.chdir('D:\Python Learn\Semester 2\[PROJECT] Fishing Game\database')
# print(6 * 0.5)
file = "fishList.csv"
df = pd.read_csv(file)


def submit():
    area =entry_area.get()
    fish_name = entry_name.get()
    weight = entry_weight.get()
    exp = entry_exp.get()
    value = entry_value.get()
    

    
    df.loc[len(df.index)] = [area, fish_name, weight, exp, value, rd.randint(2, 10)]

    df.to_csv(file, index=False)
    
    entry_area.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_exp.delete(0, tk.END)
    entry_value.delete(0, tk.END)
    
    entry_area.focus_set()
    

window = tk.Tk()
window.title("Fish Details")
window.geometry("250x250")
window.resizable(False, False)
getcontext().prec = 4  


def calculate_value(event):
    try:
        weight = float(entry_weight.get())
        exp = int(entry_exp.get())
        value = float(dec(f"{exp}") // dec(f"{weight}"))
        entry_value.delete(0, tk.END)
        entry_value.insert(0, str(value))
    except ValueError:
        entry_value.delete(0, tk.END)
        entry_value.insert(0, "Invalid Input")


window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
position_right = int(window.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(window.winfo_screenheight() / 2 - window_height / 2)
window.geometry("+{}+{}".format(position_right, position_down))

label_area = tk.Label(window, text="Area:")
label_area.pack()

entry_area = tk.Entry(window, justify="center")
entry_area.pack()

label_name = tk.Label(window, text="Fish Name:")
label_name.pack()

entry_name = tk.Entry(window, justify="center")
entry_name.pack()

label_weight = tk.Label(window, text="Weight:")
label_weight.pack()

entry_weight = tk.Entry(window, justify="center")
entry_weight.pack()

label_exp = tk.Label(window, text="EXP:")
label_exp.pack()

entry_exp = tk.Entry(window, justify="center")
entry_exp.pack()

entry_weight.bind("<KeyRelease>", calculate_value)
entry_exp.bind("<KeyRelease>", calculate_value)

label_value = tk.Label(window, text="Value:")
label_value.pack()

entry_value = tk.Entry(window, justify="center")
entry_value.pack()

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(pady=10)

window.mainloop()
