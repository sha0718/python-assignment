def fulfill_order(inventory, order, budget):
    """
    Determines if an order can be fulfilled (fully or partially) within a customer's budget.

    :param inventory: Dictionary of product: {'quantity': int, 'price': float}
    :param order: Dictionary of product: quantity_requested
    :param budget: Customer's total budget
    :return: A tuple of (status, order_fulfilled, total_cost)
    """

    # Step 1: Sort order items by price (cheapest first)
    sorted_items = sorted(order.items(), key=lambda item: inventory[item[0]]['price'])

    total_cost = 0.0
    order_fulfilled = {}
    fully_fulfilled = True

    for item, qty_requested in sorted_items:
        if item not in inventory:
            # Item not available at all
            fully_fulfilled = False
            continue

        available_qty = inventory[item]['quantity']
        unit_price = inventory[item]['price']

        # Determine how many units can be afforded and are available
        qty_to_fulfill = min(qty_requested, available_qty)
        max_affordable_qty = int((budget - total_cost) // unit_price)
        final_qty = min(qty_to_fulfill, max_affordable_qty)

        if final_qty == 0:
            # Can't afford even one
            fully_fulfilled = False
            continue

        order_fulfilled[item] = final_qty
        total_cost += final_qty * unit_price

        if final_qty < qty_requested:
            fully_fulfilled = False

    if not order_fulfilled:
        return "Impossible to Fulfill", {}, 0.0
    elif fully_fulfilled:
        return "Fully Fulfilled", order_fulfilled, total_cost
    else:
        return "Partially Fulfilled", order_fulfilled, total_cost


# Example inventory and order
inventory = {
    'Laptop': {'quantity': 5, 'price': 1000},
    'Mouse': {'quantity': 50, 'price': 25},
    'Keyboard': {'quantity': 20, 'price': 45}
}

order = {
    'Laptop': 1,
    'Mouse': 2,
    'Keyboard': 1
}

budget = 1100

# Run the fulfillment function
status, fulfilled_items, cost = fulfill_order(inventory, order, budget)

# Output result
print(f"Order Status: {status}")
print(f"Items Fulfilled: {fulfilled_items}")
print(f"Total Cost: ${cost:.2f}")
