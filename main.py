import tkinter as tk
from tkinter import messagebox, ttk
from backend import Expense, StorageManager, ExpenseCalculator

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Daily Expenses Calculator")
        self.geometry("500x400")
        self.storage = StorageManager()
        self.calculator = ExpenseCalculator()
        self.create_widgets()
        self.refresh_list()

    def create_widgets(self):
        tk.Label(self, text="Сума:").pack(pady=5)
        self.entry_amount = tk.Entry(self)
        self.entry_amount.pack()

        tk.Label(self, text="Категорія:").pack(pady=5)
        self.entry_category = tk.Entry(self)
        self.entry_category.pack()

        tk.Button(self, text="Зберегти", command=self.save_expense).pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Sum", "Cat", "Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Sum", text="Сума")
        self.tree.heading("Cat", text="Категорія")
        self.tree.heading("Date", text="Дата")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.lbl_total = tk.Label(self, text="Всього: 0")
        self.lbl_total.pack(pady=10)

    def save_expense(self):
        try:
            amt = float(self.entry_amount.get())
            cat = self.entry_category.get()
            self.storage.add_expense(Expense(amt, cat))
            self.refresh_list()
        except:
            messagebox.showerror("Помилка", "Введіть число")

    def refresh_list(self):
        for row in self.tree.get_children(): self.tree.delete(row)
        data = self.storage.get_all_expenses()
        for row in data: self.tree.insert("", tk.END, values=row)
        self.lbl_total.config(text=f"Всього: {self.calculator.calculate_total(data)}")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
