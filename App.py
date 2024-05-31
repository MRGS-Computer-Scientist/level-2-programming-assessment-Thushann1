import tkinter as tk
from tkinter import ttk
<<<<<<< HEAD
from app_settings import bg_color, bg_color1, w_width,w_height

class ExpenseTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("ExTra - Expense Tracker")
        self.geometry(f"{w_width}x{w_height}")
        self.configure(bg=bg_color)
        
        # Expense amount
        self.expense_amount_label = tk.Label(self, text="Expense amount:", bg=bg_color)
        self.expense_amount_label.place(x=50, y=50)
        self.expense_amount_entry = tk.Entry(self, width=30)
        self.expense_amount_entry.place(x=200, y=50)
        
        # Item Description
        self.item_description_label = tk.Label(self, text="Item Description:", bg=bg_color)
        self.item_description_label.place(x=50, y=100)
        self.item_description_entry = tk.Entry(self, width=30)
        self.item_description_entry.place(x=200, y=100)
        
        # Date
        self.date_label = tk.Label(self, text="Date:", bg=bg_color)
        self.date_label.place(x=50, y=150)
        self.date_entry = tk.Entry(self, width=30)
        self.date_entry.place(x=200, y=150)
        
        # Add Expense button
        self.add_expense_button = tk.Button(self, text="Add Expense", width=20)
        self.add_expense_button.place(x=200, y=200)
        
        # List of items
        self.list_of_items_label = tk.Label(self, text="List of items", bg=bg_color)
        self.list_of_items_label.place(x=500, y=50)
        self.list_of_items = tk.Listbox(self, width=40, height=10)
        self.list_of_items.place(x=500, y=80)
        
        # Transactions
        self.transactions_label = tk.Label(self, text="Transactions:", bg=bg_color)
        self.transactions_label.place(x=50, y=250)
        self.transactions_list = tk.Listbox(self, width=50, height=10)
        self.transactions_list.place(x=50, y=280)
        
        # Daily, Weekly, Monthly buttons
        self.time_frame = tk.StringVar()
        self.time_frame.set("Daily")
        
        self.daily_button = tk.Radiobutton(self, text="Daily", variable=self.time_frame, value="Daily", bg=bg_color)
        self.daily_button.place(x=200, y=250)
        
        self.weekly_button = tk.Radiobutton(self, text="Weekly", variable=self.time_frame, value="Weekly", bg=bg_color)
        self.weekly_button.place(x=260, y=250)
        
        self.monthly_button = tk.Radiobutton(self, text="Monthly", variable=self.time_frame, value="Monthly", bg=bg_color)
        self.monthly_button.place(x=340, y=250)
        
        # Edit Expense button
        self.edit_expense_button = tk.Button(self, text="Edit Expense", width=20)
        self.edit_expense_button.place(x=500, y=300)
        
        # Delete Expense button
        self.delete_expense_button = tk.Button(self, text="Delete Expense", width=20)
        self.delete_expense_button.place(x=500, y=350)
        
        # Save Expense button
        self.save_expense_button = tk.Button(self, text="Save Expense", width=20)
        self.save_expense_button.place(x=500, y=400)
        
        # Show Chart button
        self.show_chart_button = tk.Button(self, text="Show Chart", width=20)
        self.show_chart_button.place(x=500, y=450)
=======
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
>>>>>>> f898b5b453a2936208158517c30987b3f237b42e