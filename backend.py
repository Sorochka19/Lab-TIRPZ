import sqlite3
from datetime import date

# Згідно Lab_03: Клас-модель, що представляє одну витрату 
class Expense:
    def __init__(self, amount, category, expense_date=None):
        self.amount = amount
        self.category = category
        self.date = expense_date if expense_date else date.today().strftime("%Y-%m-%d")

# Згідно Lab_03: Клас, відповідальний за взаємодію з базою даних [cite: 340]
class StorageManager:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            date TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    # Згідно Lab_03: Метод add_expense, що виконує SQL INSERT 
    def add_expense(self, expense: Expense):
        query = "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)"
        self.conn.execute(query, (expense.amount, expense.category, expense.date))
        self.conn.commit()
        print("Data saved to DB") # Лог для перевірки

    def get_all_expenses(self):
        cursor = self.conn.execute("SELECT * FROM expenses")
        return cursor.fetchall()

# Згідно Lab_03: Клас, що інкапсулює бізнес-логіку [cite: 341]
class ExpenseCalculator:
    def calculate_total(self, expenses):
        total = 0
        for row in expenses:
            total += row[1] # row[1] is amount
        return total
