import tkinter as tk
from datetime import datetime
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app_settings import bg_color, bg_color1, w_width, w_height
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class ExpenseTracker(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title("ExTra - Expense Tracker")
        self.geometry(f"{w_width}x{w_height}")
        self.configure(bg=bg_color)
        
        self.current_frame = "Home"
        
        # Frames
        self.expenses = []

        # Home Frame
        self.home_frame = tk.Frame(self, background=bg_color, width=w_width, height=w_height)
        self.home_frame.place(x=0, y=0)

        # Expense amount
        self.expense_amount_label = tk.Label(self.home_frame, text="Expense amount:", bg=bg_color, fg=bg_color1)
        self.expense_amount_label.place(x=50, y=50)
        self.expense_amount_entry = tk.Entry(self.home_frame, width=30)
        self.expense_amount_entry.place(x=200, y=50)
        
        # Item Description
        self.item_description_label = tk.Label(self.home_frame, text="Item Description:", bg=bg_color, fg=bg_color1)
        self.item_description_label.place(x=50, y=100)
        self.item_description_entry = tk.Entry(self.home_frame, width=30)
        self.item_description_entry.place(x=200, y=100)
        
        # Date
        self.date_label = tk.Label(self.home_frame, text="Date:(YYYY-MM-DD)", bg=bg_color, fg=bg_color1)
        self.date_label.place(x=50, y=150)
        self.date_entry = tk.Entry(self.home_frame, width=30)
        self.date_entry.place(x=200, y=150)
        
        # Add Expense button
        self.add_expense_button = tk.Button(self.home_frame, text="Add Expense", width=20, bg=bg_color1, fg=bg_color, command=self.add_expense)
        self.add_expense_button.place(x=200, y=200)
        
        # List of items
        self.list_of_items_label = tk.Label(self.home_frame, text="List of items", bg=bg_color, fg=bg_color1)
        self.list_of_items_label.place(x=500, y=50)
        self.list_of_items = tk.Listbox(self.home_frame, width=40, height=10)
        self.list_of_items.place(x=500, y=80)
        
        # Transactions
        self.transactions_label = tk.Label(self.home_frame, text="Transactions:", bg=bg_color, fg=bg_color1)
        self.transactions_label.place(x=50, y=250)
        self.transactions_list = tk.Listbox(self.home_frame, width=50, height=10)
        self.transactions_list.place(x=50, y=280)
        
        # Edit Expense button
        self.edit_expense_button = tk.Button(self.home_frame, text="Edit Expense", width=20, bg=bg_color1, fg=bg_color, command=self.edit_expense)
        self.edit_expense_button.place(x=500, y=300)
        
        # Delete Expense button
        self.delete_expense_button = tk.Button(self.home_frame, text="Delete Expense", width=20, bg=bg_color1, fg=bg_color, command=self.delete_expense)
        self.delete_expense_button.place(x=500, y=350)
        
        # Show Chart button
        self.show_chart_button = tk.Button(self.home_frame, text="Show Chart", width=20, bg=bg_color1, fg=bg_color, command=lambda: self.go_to_frame("Chart"))
        self.show_chart_button.place(x=500, y=400)
        
        # Exit button
        self.exit_button = tk.Button(self.home_frame, text="Exit", width=20, bg=bg_color1, fg=bg_color, command=self.exit)
        self.exit_button.place(x=500, y=450)

        # Chart Frame
        self.chart_frame = tk.Frame(self, background=bg_color, width=w_width, height=w_height)

        self.back_button = tk.Button(self.chart_frame, text="Back", width=20, bg=bg_color1, fg=bg_color, command=lambda: self.go_to_frame("Home"))
        self.back_button.place(x=50, y=50)
        
        self.chart_label = tk.Label(self.chart_frame, text="ExTra Expense Chart", font=("arial", 25), bg=bg_color)
        self.chart_label.place(x=300, y=50)
        
        # Initialize chart_canvas
        self.chart_canvas = None


    # Exit button
    def exit(self):
        confirm_exit = messagebox.askquestion("askquestion", "Are you sure?")
        if confirm_exit == 'yes':
            self.destroy()

    # Switch Frame (switching to the chart frame)
    def go_to_frame(self, next_frame):
        if self.current_frame == "Home":
            self.home_frame.place_forget()
        elif self.current_frame == "Chart":
            self.chart_frame.place_forget()

        if next_frame == "Chart":
            self.chart_frame.place(x=0, y=0)
            self.current_frame = "Chart"
            self.show_pie_chart()
        elif next_frame == "Home":
            self.home_frame.place(x=0, y=0)
            self.current_frame = "Home"

    # Add expense entry (with error prevention)
    def add_expense(self):
        amount = self.expense_amount_entry.get()
        description = self.item_description_entry.get()
        date = self.date_entry.get()
        if not amount or not description or not date:
            messagebox.showerror("Error", "All fields must be filled out")
            return
        if not self.validate_date(date):
            messagebox.showerror("Error", "Date format must be YYYY-MM-DD")
            return
        if not self.validate_amount(amount):
            messagebox.showerror("Error", "Amount must be a number")
            return
        self.expenses.append((float(amount), description, date))
        self.transactions_list.insert(tk.END, f"{date} - {description}: ${amount}")
        self.list_of_items.insert(tk.END, f"{date} - {description}: ${amount}")
        self.clear_entries()


    # Edit expense entry (with error prevention)
    def edit_expense(self):
        selected = self.transactions_list.curselection()
        selected = self.list_of_items.curselection()
        if not selected:
            messagebox.showerror("Error", "No expense selected")
            return
        index = selected[0]
        amount, description, date = self.expenses[index]
        self.expense_amount_entry.insert(0, amount)
        self.item_description_entry.insert(0, description)
        self.date_entry.insert(0, date)
        self.delete_expense()


    # Delete expense entry (with error prevention)
    def delete_expense(self):
        selected = self.transactions_list.curselection()
        selected = self.list_of_items.curselection()
        if not selected:
            messagebox.showerror("Error", "No expense selected")
            return
        index = selected[0]
        del self.expenses[index]
        self.transactions_list.delete(index)
        self.list_of_items.delete(index)


    # Validating The dates code
    def validate_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    # validating amount (if its not in numbers error prevention)
    def validate_amount(self, amount):
        try:
            float(amount)
            return True
        except ValueError:
            return False
        

      # clearing entries after Adding the expense input  
    def clear_entries(self):
        self.expense_amount_entry.delete(0, tk.END)
        self.item_description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)


    # pie chart canvas
    def show_pie_chart(self):
        if self.chart_canvas:
            self.chart_canvas.get_tk_widget().destroy()
        
        labels = [expense[1] for expense in self.expenses]
        sizes = [expense[0] for expense in self.expenses]
        
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        
        self.chart_canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().place(x=200, y=150)

if __name__ == "__main__":
    app = ExpenseTracker()
    app.mainloop()
