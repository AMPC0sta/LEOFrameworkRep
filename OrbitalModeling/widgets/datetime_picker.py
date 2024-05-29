import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class DateTimePicker(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.date_label = ttk.Label(self, text="Date:")
        self.date_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        self.date_entry = DateEntry(self,selectmode='day', date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1, padx=1, pady=5)
        
        self.time_label = ttk.Label(self, text="Time:")
        self.time_label.grid(row=0, column=2, padx=1, pady=5, sticky="e")
        
        self.hour_var = tk.StringVar()
        self.hour_combobox = ttk.Combobox(self, values=[f"{i:02d}" for i in range(24)], width=3, textvariable=self.hour_var)
        self.hour_combobox.grid(row=0, column=2, padx=1, pady=5, sticky="w")
        
        self.minute_var = tk.StringVar()
        self.minute_combobox = ttk.Combobox(self, values=[f"{i:02d}" for i in range(60)], width=3, textvariable=self.minute_var)
        self.minute_combobox.grid(row=0, column=4, padx=1, pady=5, sticky="w")
        

        # Minutes are the minimum possible resolution
        #self.second_var = tk.StringVar()
        #self.second_combobox = ttk.Combobox(self, values=[f"{i:02d}" for i in range(60)], width=3, textvariable=self.second_var)
        #self.second_combobox.grid(row=0, column=5, padx=1, pady=5, sticky="w")
        
    def get_datetime(self):
        date = self.date_entry.get_date()
        hour = int(self.hour_var.get())
        minute = int(self.minute_var.get())
        #second = int(self.second_var.get())
        second = 0
        return f"{date} {hour:02d}:{minute:02d}:{second:02d}"
