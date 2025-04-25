def record_transactions():
    """
    Records bank transactions and prints balance after each entry.
    Shows final summary at the end.
    """
    balance = 0
    transactions = []

    print("Welcome to Bank Transaction Analyzer!")
    print("Enter your transactions in the format: credit 1000 or debit 500")
    print("Type 'done' to finish and view the summary.\n")

    while True:
        user_input = input("Enter transaction: ").strip().lower()

        if user_input == "done":
            break

        # Split the input into action and amount
        try:
            action, amount_str = user_input.split()
            amount = float(amount_str)

            if action not in ['credit', 'debit'] or amount <= 0:
                raise ValueError

            if action == "credit":
                balance += amount
                transactions.append((action, amount, balance))
                print(f"Credited ₹{amount:.2f}. New Balance: ₹{balance:.2f}")
            elif action == "debit":
                balance -= amount
                transactions.append((action, amount, balance))
                print(f"Debited ₹{amount:.2f}. New Balance: ₹{balance:.2f}")

        except ValueError:
            print("Invalid input. Please use format: credit 1000 or debit 500")

    # Final Summary
    print("\nTransaction Summary:")
    total_credit = sum(t[1] for t in transactions if t[0] == "credit")
    total_debit = sum(t[1] for t in transactions if t[0] == "debit")

    for idx, (action, amount, bal) in enumerate(transactions, start=1):
        print(f"{idx}. {action.title():<6} ₹{amount:<8.2f} | Balance: ₹{bal:.2f}")

    print("\nFinal Summary:")
    print(f"Total Credits: ₹{total_credit:.2f}")
    print(f"Total Debits : ₹{total_debit:.2f}")
    print(f"Final Balance: ₹{balance:.2f}")

# Run the program
record_transactions()
