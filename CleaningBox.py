import tkinter as tk
import tkinter.ttk as ttk

class CleaningBox():
    def __init__(self):
        window =  tk.Tk()

        amount_missing = tk.StringVar()
        check_drop = tk.IntVar()

        wrapper = tk.LabelFrame(window, text="Select Column")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper2 = tk.LabelFrame(window, text="Select Options")
        wrapper2.pack(padx = 10, pady = 10, fill = "both", expand= "yes")

        cols = ["column 1", "column 2", "column 3"]
        options = ["Drop Check", "Column Name", "Data Type", "Number of Missing",  "Handle Missing Values"]
        
        label1 = tk.Label(wrapper, text = "Column")
        label1.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper, height = 15, values = cols, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1)

        lbl1 = tk.Label(wrapper2, text = "Data Type")
        lbl1.grid(row=0, column=0, padx = 10, pady=10)
        datatypes = ["Numeric", "Categorical", "Datetime"]
        combo1 = ttk.Combobox(wrapper2, height = 15, values = datatypes, width = 30)
        combo1.grid(row=0, column=1, padx=10, pady=10)

        lbl2 = tk.Label(wrapper2, text = "# of Missing Values :")
        lblMissingValues = tk.Label(wrapper2, text = amount_missing)
        lbl2.grid(row=1, column=0, padx = 10, pady=10)
        lblMissingValues.grid(row=1, column=1, padx = 10, pady=10)

        lbl3 = tk.Label(wrapper2, text = "Handle Missing Values")
        lbl3.grid(row=2, column=0, padx = 10, pady=10)

        handleMissingVals = ["Replacing With Mean", "Replacing With Median", "Others..."]
        combo2 = ttk.Combobox(wrapper2, values = handleMissingVals, height = 15,  width = 30)
        combo2.grid(row=2, column=1, padx=10, pady = 10)

        lbl4 = tk.Label(wrapper2, text = "Drop Check")
        lbl4.grid(row=3, column=0, padx = 10, pady=10)

        checkBox1 = tk.Checkbutton(wrapper2, variable=check_drop)
        checkBox1.grid(row=3, column=1, padx = 10, pady=10)

        window.title("CleaningBox")
        window.geometry("720x300")
        window.resizable(False, False)
        window.mainloop()

        


cBox = CleaningBox()
