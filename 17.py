#-   ATM withdrawal: enter balance and withdrawal amount; complete if sufficient, otherwise display "Insufficient Balance."
balance = float(input("Enter your balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))
if withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print("Withdrawal successful. Remaining balance: $", balance)
else:
    print("Insufficient Balance.")
    