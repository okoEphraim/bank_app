import tkinter as tk

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank App")
        self.geometry("300x200")

        self.balance = 0

        self.balance_label = tk.Label(self, text="Balance: $0")
        self.balance_label.pack(pady=10)

        deposit_frame = tk.Frame(self)
        deposit_frame.pack()

        deposit_label = tk.Label(deposit_frame, text="Deposit amount:")
        deposit_label.pack(side=tk.LEFT)

        self.deposit_entry = tk.Entry(deposit_frame)
        self.deposit_entry.pack(side=tk.LEFT)

        deposit_button = tk.Button(self, text="Deposit", command=self.deposit)
        deposit_button.pack(pady=5)

        withdraw_frame = tk.Frame(self)
        withdraw_frame.pack()

        withdraw_label = tk.Label(withdraw_frame, text="Withdraw amount:")
        withdraw_label.pack(side=tk.LEFT)

        self.withdraw_entry = tk.Entry(withdraw_frame)
        self.withdraw_entry.pack(side=tk.LEFT)

        withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw)
        withdraw_button.pack(pady=5)

    def deposit(self):
        amount = float(self.deposit_entry.get())
        self.balance += amount
        self.balance_label.config(text=f"Balance: ${self.balance}")
        self.deposit_entry.delete(0, tk.END)

    def withdraw(self):
        amount = float(self.withdraw_entry.get())
        if amount <= self.balance:
            self.balance -= amount
            self.balance_label.config(text=f"Balance: ${self.balance}")
        else:
            tk.messagebox.showerror("Insufficient Funds", "You do not have enough balance.")
        self.withdraw_entry.delete(0, tk.END)

# Create an instance of the BankApp class
app = BankApp()
app.mainloop()
