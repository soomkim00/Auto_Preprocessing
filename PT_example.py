import tkinter as tk
from tkinter import ttk
import pandas as pd

root = tk.Tk()

sample = {"File Name":[f"file_{i}" for i in range(5)],
          'Sheet Name': [f"sheet_{i}" for i in range(5)],
          'Number Of Rows': [f"row_{i}" for i in range(5)],
          'Number Of Columns': [f"col_{i}" for i in range(5)]
          }
df = pd.DataFrame(sample)
cols = list(df.columns)

tree = ttk.Treeview(root)
tree.pack()
tree["columns"] = cols
for i in cols:
    tree.column(i, anchor="w")
    tree.heading(i, text=i, anchor='w')

for index, row in df.iterrows():
    tree.insert("",0,text=index,values=list(row))

root.mainloop()