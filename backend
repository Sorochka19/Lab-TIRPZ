import sqlite3
from datetime import date

class Expense:
    def __init__(self, amount, category, expense_date=None):
        # amount (float): Сума витрати
        self.amount = amount
        # category (str): Категорія витрати (наприклад, "Їжа", "Транспорт")
        self.category = category
        # date (str): Дата витрати (формат YYYY-MM-DD)
        self.date = expense_date if expense_date else date.today().strftime("%Y-%m-%d")

class StorageManager:
    def __init__(self, db_name="expenses.db"):
        # Підключення до бази даних SQLite
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        # Створення таблиці, якщо вона не існує
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

    def add_expense(self, expense: Expense):
        query = "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)"
        self.conn.execute(query, (expense.amount, expense.category, expense.date))
        self.conn.commit()
        # print("Data saved to DB") # Можна залишити для логування, якщо треба

    def get_all_expenses(self):
        cursor = self.conn.execute("SELECT id, amount, category, date FROM expenses ORDER BY date DESC")
        return cursor.fetchall()
    
    def close(self):
        self.conn.close()

class ExpenseCalculator:
    def calculate_total(self, expenses):
        total = 0.0
        for row in expenses:
            total += row[1] 
        return round(total, 2)



if __name__ == '__main__':
    storage = StorageManager()
    calculator = ExpenseCalculator()
    
    storage.add_expense(Expense(amount=150.50, category="Їжа"))
    storage.add_expense(Expense(amount=45.00, category="Транспорт"))
    
    all_expenses = storage.get_all_expenses()
    print("Всі витрати:", all_expenses)
    
    total_sum = calculator.calculate_total(all_expenses)
    print(f"Загальна сума витрат: {total_sum}")
    
    storage.close()
