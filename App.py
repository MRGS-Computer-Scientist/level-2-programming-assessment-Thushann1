import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt

# Main Application Class
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ExTra - Expense Tracker")
        self.root.geometry("800x600")
        
        # Main frame setup
        self.main_frame = tk.Frame(root, bg="#d3d3d3")
        self.main_frame.pack(fill="both", expand=True)
        
        # Expense input fields
        # Label and Entry for Expense Amount
        tk.Label(self.main_frame, text="Expense Amount ($):", bg="#d3d3d3").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.expense_amount = tk.Entry(self.main_frame)
        self.expense_amount.grid(row=0, column=1, padx=10, pady=10)
        
        # Label and Entry for Item Description
        tk.Label(self.main_frame, text="Item Description:", bg="#d3d3d3").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.item_description = tk.Entry(self.main_frame)
        self.item_description.grid(row=1, column=1, padx=10, pady=10)
        
        # Label and DateEntry for Date
        tk.Label(self.main_frame, text="Date:", bg="#d3d3d3").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.date_entry = DateEntry(self.main_frame, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Buttons
        # Button to Add Expense
        tk.Button(self.main_frame, text="Add Expense", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=10)
        # Button to Edit Selected Expense
        tk.Button(self.main_frame, text="Edit Expense", command=self.edit_expense).grid(row=4, column=0, columnspan=2, pady=10)
        # Button to Delete Selected Expense
        tk.Button(self.main_frame, text="Delete Expense", command=self.delete_expense).grid(row=5, column=0, columnspan=2, pady=10)
        # Button to Save Expenses
        tk.Button(self.main_frame, text="Save Expense", command=self.save_expense).grid(row=6, column=0, columnspan=2, pady=10)
        # Button to Show Expense Chart
        tk.Button(self.main_frame, text="Show Chart", command=self.show_chart).grid(row=7, column=0, columnspan=2, pady=10)
        
        # Transactions list
        # Label for Transactions
        self.transactions_label = tk.Label(self.main_frame, text="Transactions:", bg="#d3d3d3")
        self.transactions_label.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Listbox to Display Transactions
        self.transactions_list = tk.Listbox(self.main_frame, height=10, width=50)
        self.transactions_list.grid(row=9, column=0, columnspan=2, pady=10)
        
        # Sample data for the chart
        self.expenses = {
            "Utilities (needs)": 63,
            "Savings": 15,
            "Misc": 22
        }
        
        # Transaction storage
        self.transactions = []

    # Method to Add Expense
    def add_expense(self):
        amount = self.expense_amount.get()
        description = self.item_description.get()
        date = self.date_entry.get()
        
        if not amount or not description or not date:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return
        
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid amount.")
            return
        
        transaction = f"{date} - {description}: ${amount:.2f}"
        self.transactions.append(transaction)
        self.transactions_list.insert(tk.END, transaction)
        self.clear_inputs()
        messagebox.showinfo("Success", "Expense added successfully!")

    # Method to Clear Input Fields
    def clear_inputs(self):
        self.expense_amount.delete(0, tk.END)
        self.item_description.delete(0, tk.END)
        self.date_entry.set_date(dt.datetime.now())

    # Method to Edit Selected Expense
    def edit_expense(self):
        selected = self.transactions_list.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a transaction to edit.")
            return
        
        transaction = self.transactions[selected[0]]
        date, rest = transaction.split(" - ")
        description, amount = rest.split(": $")
        
        self.date_entry.set_date(date)
        self.item_description.insert(0, description)
        self.expense_amount.insert(0, amount)

        self.transactions.pop(selected[0])
        self.transactions_list.delete(selected[0])
        messagebox.showinfo("Edit Mode", "Edit the fields and click 'Add Expense' to save changes.")

    # Method to Delete Selected Expense
    def delete_expense(self):
        selected = self.transactions_list.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a transaction to delete.")
            return
        
        self.transactions.pop(selected[0])
        self.transactions_list.delete(selected[0])
        messagebox.showinfo("Deleted", "Expense deleted successfully!")

    # Method to Save Expenses
    def save_expense(self):
        # This function can be implemented to save expenses to a file or database
        messagebox.showinfo("Save Expense", "Expenses saved successfully!")

    # Method to Show Expense Chart
    def show_chart(self):
        fig, ax = plt.subplots()
        labels = self.expenses.keys()
        sizes = self.expenses.values()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        
        chart_window = tk.Toplevel(self.root)
        chart_window.title("Expense Chart")
        
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
