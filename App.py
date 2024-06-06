import tkinter as tk
from tkinter import ttk
from app_settings import bg_color, bg_color1, w_width, w_height
from tkinter import messagebox

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
        self.home_frame = tk.Frame(self, background=bg_color, width=w_width, height=(w_height-200))
        self.home_frame.place(x=0, y=0)

        # Expense amount
        self.expense_amount_label = tk.Label(self, text="Expense amount:", bg=bg_color, fg=bg_color1)
        self.expense_amount_label.place(x=50, y=50)
        self.expense_amount_entry = tk.Entry(self, width=30)
        self.expense_amount_entry.place(x=200, y=50)
        
        # Item Description
        self.item_description_label = tk.Label(self, text="Item Description:", bg=bg_color, fg=bg_color1)
        self.item_description_label.place(x=50, y=100)
        self.item_description_entry = tk.Entry(self, width=30)
        self.item_description_entry.place(x=200, y=100)
        
        # Date
        self.date_label = tk.Label(self, text="Date:(YYYY/MM/DD)", bg=bg_color, fg=bg_color1)
        self.date_label.place(x=50, y=150)
        self.date_entry = tk.Entry(self, width=30)
        self.date_entry.place(x=200, y=150)
        
        # Add Expense button
        self.add_expense_button = tk.Button(self, text="Add Expense", width=20, bg=bg_color1, fg=bg_color)
        self.add_expense_button.place(x=200, y=200)
        
        # List of items
        self.list_of_items_label = tk.Label(self, text="List of items", bg=bg_color, fg=bg_color1)
        self.list_of_items_label.place(x=500, y=50)
        self.list_of_items = tk.Listbox(self, width=40, height=10)
        self.list_of_items.place(x=500, y=80)
        
        # Transactions
        self.transactions_label = tk.Label(self, text="Transactions:", bg=bg_color, fg=bg_color1)
        self.transactions_label.place(x=50, y=250)
        self.transactions_list = tk.Listbox(self, width=50, height=10)
        self.transactions_list.place(x=50, y=280)
        
        # Daily, Weekly, Monthly buttons
        self.time_frame = tk.StringVar()
        self.time_frame.set("Daily")
        
        self.daily_button = tk.Radiobutton(self, text="Daily", variable=self.time_frame, value="Daily", bg=bg_color, fg=bg_color1)
        self.daily_button.place(x=200, y=250)
        
        self.weekly_button = tk.Radiobutton(self, text="Weekly", variable=self.time_frame, value="Weekly", bg=bg_color, fg=bg_color1)
        self.weekly_button.place(x=260, y=250)
        
        self.monthly_button = tk.Radiobutton(self, text="Monthly", variable=self.time_frame, value="Monthly", bg=bg_color, fg=bg_color1)
        self.monthly_button.place(x=340, y=250)
        
        # Edit Expense button
        self.edit_expense_button = tk.Button(self, text="Edit Expense", width=20, bg=bg_color1, fg=bg_color)
        self.edit_expense_button.place(x=500, y=300)
        
        # Delete Expense button
        self.delete_expense_button = tk.Button(self, text="Delete Expense", width=20, bg=bg_color1, fg=bg_color)
        self.delete_expense_button.place(x=500, y=350)
        
        # Save Expense button
        self.save_expense_button = tk.Button(self, text="Save Expense", width=20, bg=bg_color1, fg=bg_color)
        self.save_expense_button.place(x=500, y=400)
        
        # Show Chart button
        self.show_chart_button = tk.Button(self, text="Show Chart", width=20, bg=bg_color1, fg=bg_color, command=lambda: self.go_to_frame("Chart"))
        self.show_chart_button.place(x=500, y=450)

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", width=20, bg=bg_color1, fg=bg_color, command=self.exit)
        self.exit_button.place(x=500, y=500)

        # Chart Frame
        self.chart_frame = tk.Frame(self, background=bg_color, width=w_width, height=(w_height-200))

        # Asks confirmation from user before exiting/destroying the app
    def exit(self):
        confirm_exit = messagebox.askquestion("askquestion", "Are you sure?")
        if confirm_exit == 'yes':
            self.destroy()

    def go_to_frame(self, next_frame):
        if self.current_frame == "Home":
            self.home_frame.place_forget()
        elif self.current_frame == "Chart":
            self.chart_frame.place_forget()

        if next_frame == "Chart":
            self.chart_frame.place(x=0, y=0)
            self.current_frame = "Chart"
        elif next_frame == "Home":
            self.home_frame.place(x=0, y=0)
            self.current_frame = "Home"

if __name__ == "__main__":
    app = ExpenseTracker()
    app.mainloop()
