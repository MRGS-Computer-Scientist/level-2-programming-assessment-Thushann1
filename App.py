import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ExTra - Expense Tracker")
        self.root.geometry("800x600")
        
        # Main frame
        self.main_frame = tk.Frame(root, bg="#d3d3d3")
        self.main_frame.pack(fill="both", expand=True)
        
        # Putting your expenses in
        tk.Label(self.main_frame, text="Expense amount:", bg="#d3d3d3").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.expense_amount = tk.Entry(self.main_frame)
        self.expense_amount.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.main_frame, text="Item Description:", bg="#d3d3d3").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.item_description = tk.Entry(self.main_frame)
        self.item_description.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.main_frame, text="Date:", bg="#d3d3d3").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.date_entry = datetime(self.main_frame, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)
                
        # Buttons
        tk.Button(self.main_frame, text="Add Expense", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.main_frame, text="Edit Expense", command=self.edit_expense).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.main_frame, text="Delete Expense", command=self.delete_expense).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.main_frame, text="Save Expense", command=self.save_expense).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.main_frame, text="Show Chart", command=self.show_chart).grid(row=7, column=0, columnspan=2, pady=10)


#main
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
