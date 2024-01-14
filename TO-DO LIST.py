import tkinter as tk
from tkinter import messagebox, simpledialog
class FancyTodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do List😎")
        self.tasks = []
        self.task_entry = tk.Entry(root, width=30, font=("Verdana", 12))
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Verdana", 12), bg="#ffe0b2", selectbackground="#ffcc80", width=40)
        self.add_button = tk.Button(root, text=" 📃 Add Task", command=self.add_task, font=("Verdana", 12, "bold"), bg="#4CAF50", fg="white")
        self.edit_button = tk.Button(root, text="✒️ Edit Task", command=self.edit_task, font=("Verdana", 12, "bold"), bg="#2196F3", fg="white")
        self.complete_button = tk.Button(root, text="✔ Mark Complete", command=self.mark_complete, font=("Verdana", 12, "bold"), bg="#2196F3", fg="white")
        self.delete_button = tk.Button(root, text="👎 Delete Task", command=self.delete_task, font=("Verdana", 12, "bold"), bg="#E53935", fg="white")
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        self.add_button.grid(row=0, column=4, padx=10, pady=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=5)
        self.edit_button.grid(row=2, column=0, padx=5, pady=5)
        self.complete_button.grid(row=2, column=1, padx=5, pady=5)
        self.delete_button.grid(row=2, column=2, padx=5, pady=5)
        self.task_listbox.bind("<<ListboxSelect>>", self.on_task_select)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append({"text": task_text, "complete": False})
            self.update_task_list()
            self.clear_entry()
    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_text = simpledialog.askstring("Edit Task", "✏ Edit task:", initialvalue=self.tasks[selected_index[0]]["text"], height=3)
            if new_text:
                self.tasks[selected_index[0]] = {"text": new_text, "complete": False}
                self.update_task_list()
    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["complete"] = not self.tasks[selected_index[0]]["complete"]
            self.update_task_list()
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_list()
    def clear_entry(self):
        self.task_entry.delete(0, tk.END)
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["text"]
            if task["complete"]:
                task_text += " ✔ (Complete)"
                self.task_listbox.insert(tk.END, task_text)
                self.task_listbox.itemconfig(tk.END, {'bg': '#81C784', 'fg': 'white'})
            else:
                self.task_listbox.insert(tk.END, task_text)
    def on_task_select(self, event):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            self.clear_entry()
        else:
            selected_task = self.tasks[selected_index[0]]["text"]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, selected_task)
if __name__ == "__main__":
    root = tk.Tk()
    app = FancyTodoListApp(root)
    root.configure(bg="#D2D2D2") 
    root.mainloop()
