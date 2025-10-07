import pandas as pd
import os

# --- Expense class ---
class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = float(amount)
        self.date = date

# --- ExpenseManager class ---
class ExpenseManager:
    def __init__(self, filename="expenses.csv"):
        self.expenses = []
        self.filename = filename
        self.load_from_csv()

    def add_expense(self, category, amount, date):
        expense = Expense(category, amount, date)
        self.expenses.append(expense)
        print("✅ Expense added!")

    def view_expenses(self):
        if not self.expenses:
            print("❌ No expenses to show.")
            return

        print("\n--- All Expenses ---")
        for i, e in enumerate(self.expenses, 1):
            print(f"{i}. {e.category} | ${e.amount:.2f} | {e.date}")

    def category_summary(self):
        if not self.expenses:
            print("❌ No expenses to summarize.")
            return

        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount

        print("\n--- Total Spent per Category ---")
        for cat, total in summary.items():
            print(f"{cat}: ${total:.2f}")

    def save_to_csv(self):
        if not self.expenses:
            print("❌ No data to save.")
            return

        data = [{'Category': e.category, 'Amount': e.amount, 'Date': e.date} for e in self.expenses]
        df = pd.DataFrame(data)
        df.to_csv(self.filename, index=False)
        print(f"💾 Saved {len(self.expenses)} expenses to '{self.filename}'")

    def load_from_csv(self):
        if not os.path.exists(self.filename):
            print(f"ℹ️ File '{self.filename}' not found. Starting fresh.")
            return

        try:
            df = pd.read_csv(self.filename)
            self.expenses = []
            for _, row in df.iterrows():
                self.expenses.append(Expense(row['Category'], row['Amount'], row['Date']))
            print(f"📂 Loaded {len(self.expenses)} expenses from '{self.filename}'")
        except Exception as e:
            print("❌ Error loading file:", e)

# --- Main Program ---
def main():
    manager = ExpenseManager()

    while True:
        print(f"\n--- Expense Tracker Menu (Total: {len(manager.expenses)} expenses) ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total per Category")
        print("4. Save to CSV")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()

        if choice == '1':
            category = input("Enter category: ").strip()
            amount = input("Enter amount: ").strip()
            date = input("Enter date (e.g., 2025-10-07): ").strip()
            manager.add_expense(category, amount, date)

        elif choice == '2':
            manager.view_expenses()

        elif choice == '3':
            manager.category_summary()

        elif choice == '4':
            manager.save_to_csv()

        elif choice == '5':
            manager.save_to_csv()
            print("👋 Exiting. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose 1–5.")

if __name__ == "__main__":
    main()