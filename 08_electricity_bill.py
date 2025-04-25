def calculate_electricity_bill(units):
    """
    Calculates the electricity bill based on slab-wise unit rates.

    :param units: Total electricity consumed in kWh
    :return: A detailed string showing the bill breakdown and total
    """
    total_amount = 0
    bill_breakdown = []

    # First slab: 0-100 units @ ₹5/unit
    if units > 0:
        slab_units = min(units, 100)
        amount = slab_units * 5
        total_amount += amount
        bill_breakdown.append(f"0-100 units @ ₹5/unit = ₹{amount}")

    # Second slab: 101-300 units @ ₹7/unit
    if units > 100:
        slab_units = min(units - 100, 200)
        amount = slab_units * 7
        total_amount += amount
        bill_breakdown.append(f"101-300 units @ ₹7/unit = ₹{amount}")

    # Third slab: 301-500 units @ ₹10/unit
    if units > 300:
        slab_units = min(units - 300, 200)
        amount = slab_units * 10
        total_amount += amount
        bill_breakdown.append(f"301-500 units @ ₹10/unit = ₹{amount}")

    # Fourth slab: above 500 units @ ₹15/unit
    if units > 500:
        slab_units = units - 500
        amount = slab_units * 15
        total_amount += amount
        bill_breakdown.append(f"501+ units @ ₹15/unit = ₹{amount}")

    # Display the bill breakdown
    print("Electricity Bill Breakdown:")
    for line in bill_breakdown:
        print(line)

    print(f"\nTotal Amount Payable = ₹{total_amount}")

# Input from user
try:
    usage = int(input("Enter electricity usage in kWh: "))
    if usage < 0:
        print("Usage cannot be negative.")
    else:
        calculate_electricity_bill(usage)
except ValueError:
    print("Please enter a valid integer for electricity usage.")
