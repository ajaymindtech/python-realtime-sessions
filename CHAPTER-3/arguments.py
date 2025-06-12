def calculate_total(*prices, tax_rate=0.1):
    subtotal = sum(prices)
    print(f"Subtotal: {subtotal}, Tax Rate: {tax_rate}")
    tax = subtotal * tax_rate
    print(f"Tax: {tax}")
    print(f"Total: {subtotal + tax}")
    return subtotal + tax

print(calculate_total(10, 20, 30, tax_rate=0.2))  # Output: 72.0