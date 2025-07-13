#!/usr/bin/env python3
"""
Number System Converter
Converts between Decimal, Binary, Octal and Hexadecimal.

"""

import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ Conversion Logic ------------------ #
def convert_number(value: str, from_base: str, to_base: str) -> str:
    """Convert 'value' (string) from one base to another and return result string."""
    bases = {"Binary": 2, "Octal": 8, "Decimal": 10, "Hexadecimal": 16}

    try:
        # 1) Parse input into an integer (base → decimal)
        num = int(value, bases[from_base])
    except ValueError:
        raise ValueError(f"‘{value}’ is not a valid {from_base} number.")

    # 2) Convert decimal integer into the target base
    if to_base == "Binary":
        return bin(num)[2:]            # strip ‘0b’
    elif to_base == "Octal":
        return oct(num)[2:]            # strip ‘0o’
    elif to_base == "Hexadecimal":
        return hex(num)[2:].upper()    # strip ‘0x’ and capitalise
    else:  # Decimal
        return str(num)

# ------------------ GUI ------------------ #
class ConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number System Converter")
        self.geometry("480x260")
        self.resizable(False, False)

        # Fonts
        lbl_font = ("Arial", 12)
        ent_font = ("Consolas", 12)

        # Input value
        tk.Label(self, text="Enter Number:", font=lbl_font).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.entry_value = tk.Entry(self, font=ent_font, width=28)
        self.entry_value.grid(row=0, column=1, padx=10, pady=10)

        # From‑base dropdown
        tk.Label(self, text="Convert from:", font=lbl_font).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.combo_from = ttk.Combobox(self, font=lbl_font, state="readonly",
                                       values=["Binary", "Decimal", "Octal", "Hexadecimal"])
        self.combo_from.current(1)  # default = Decimal
        self.combo_from.grid(row=1, column=1, padx=10, pady=10)

        # To‑base dropdown
        tk.Label(self, text="Convert   to:", font=lbl_font).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.combo_to = ttk.Combobox(self, font=lbl_font, state="readonly",
                                     values=["Binary", "Decimal", "Octal", "Hexadecimal"])
        self.combo_to.current(0)  # default = Binary
        self.combo_to.grid(row=2, column=1, padx=10, pady=10)

        # Convert button
        tk.Button(self, text="Convert", font=lbl_font, width=18, command=self.perform_conversion, bg="#90EE90")\
          .grid(row=3, columnspan=2, pady=15)

        # Result label
        self.result_var = tk.StringVar()
        tk.Label(self, textvariable=self.result_var, font=("Consolas", 14, "bold"), fg="#006400")\
          .grid(row=4, columnspan=2, pady=10)

    def perform_conversion(self):
        value = self.entry_value.get().strip()
        from_base = self.combo_from.get()
        to_base = self.combo_to.get()

        if not value:
            messagebox.showwarning("Empty Input", "Please enter a number to convert.")
            return

        try:
            result = convert_number(value, from_base, to_base)
            self.result_var.set(f"{value} ({from_base})  →  {result} ({to_base})")
        except ValueError as err:
            messagebox.showerror("Invalid Number", str(err))
            self.result_var.set("")  # clear previous result


if __name__ == "__main__":
    ConverterGUI().mainloop()
