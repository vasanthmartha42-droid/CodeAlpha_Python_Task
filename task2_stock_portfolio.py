# task2_stock_portfolio.py
# CodeAlpha Python Task 2: Stock Portfolio Tracker

# Hardcoded stock prices (per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
}


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dict {stock: quantity}."""
    portfolio = {}

    print("Available stocks and prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")
    print("\nEnter your stocks one by one. Type 'done' when finished.\n")

    while True:
        name = input("Stock name (or 'done'): ").strip().upper()

        if name == "DONE":
            break

        if name not in STOCK_PRICES:
            print("Stock not found in the price list. Try again.")
            continue

        try:
            quantity = int(input(f"Quantity of {name}: "))
        except ValueError:
            print("Please enter a whole number for quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        # If the same stock is entered twice, add to the existing quantity
        portfolio[name] = portfolio.get(name, 0) + quantity

    return portfolio


def calculate_total(portfolio):
    """Returns the total investment value and a list of per-stock lines."""
    total = 0
    lines = []

    for stock, quantity in portfolio.items():
        value = STOCK_PRICES[stock] * quantity
        total += value
        lines.append(f"{stock}: {quantity} shares x ${STOCK_PRICES[stock]} = ${value}")

    return total, lines


def save_to_file(lines, total, filename="portfolio_summary.txt"):
    """Saves the portfolio summary to a text file."""
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-" * 30 + "\n")
        for line in lines:
            file.write(line + "\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total Investment: ${total}\n")
    print(f"\nSummary saved to {filename}")


def main():
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total, lines = calculate_total(portfolio)

    print("\n--- Portfolio Summary ---")
    for line in lines:
        print(line)
    print("-------------------------")
    print(f"Total Investment: ${total}")

    choice = input("\nSave result to a file? (y/n): ").strip().lower()
    if choice == "y":
        save_to_file(lines, total)


if __name__ == "__main__":
    main()
