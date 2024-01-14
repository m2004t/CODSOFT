import tkinter as tk
from tkinter import ttk
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Calculator")
        self.root.geometry("400x600")
        self.root.config(bg="#121212")
        self.entry_var = tk.StringVar()
        entry = ttk.Entry(root, textvariable=self.entry_var, font=('Orbitron', 24), justify="right", state="readonly")
        entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)
        button_bg = "#000000"
        button_fg = "#00FF00"
        button_font = ('Orbitron', 18)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('+/-', 5, 1), ('%', 5, 2), ('DEL', 5, 3),
        ]
        for (text, row, col) in buttons:
            ttk.Button(root, text=text, command=lambda t=text: self.button_click(t), style="TButton",padding=20).grid(row=row, column=col, sticky="nsew")
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
        style = ttk.Style()
        style.configure("TButton", font=button_font, foreground=button_fg, background=button_bg)
        style.map("TButton",background=[("active", "#004400")],foreground=[("active", "#00FF00")])
        self.root.bind("<Key>", self.key_press)
    def button_click(self, text):
        current_text = self.entry_var.get()
        if text == "=":
            try:
                result = str(eval(current_text))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        elif text == "C":
            self.entry_var.set("")
        elif text == "+/-":
            if current_text and current_text[0] == '-':
                self.entry_var.set(current_text[1:])
            else:
                self.entry_var.set('-' + current_text)
        elif text == "DEL":
            self.entry_var.set(current_text[:-1])
        else:
            self.entry_var.set(current_text + text)
    def key_press(self, event):
        key = event.char
        if key.isdigit() or key in "+-*/.=":
            self.button_click(key)
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
