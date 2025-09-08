import csv
def get_portfolio():
    """Collects portfolio stock symbols and quantities from user input."""
    portfolio = {}
    try:
        num_stocks = int(input("Enter the number of different stocks in your portfolio: "))
        for _ in range(num_stocks):
            stock = input("Enter stock symbol (e.g., AAPL): ").upper().strip()
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                return get_portfolio()
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        return portfolio
    except ValueError:
        print("Invalid input. Please enter numeric values for counts and quantities.")
        return get_portfolio()
def calculate_investment(portfolio, prices):
    """Calculates investment value per stock and total investment."""
    summary = {}
    total = 0
    for stock, qty in portfolio.items():
        price = prices.get(stock)
        if price is not None:
            value = price * qty
            summary[stock] = {'quantity': qty, 'price': price, 'value': value}
            total += value
        else:
            print(f"Warning: Price not found for {stock}, skipping in total calculation.")
    return summary, total
def display_summary(summary, total):
    """Prints the portfolio investment summary."""
    print("\nPortfolio Summary:")
    print(f"{'Stock':<8}{'Quantity':<10}{'Price':<10}{'Value':<10}")
    print("-" * 40)
    for stock, data in summary.items():
        print(f"{stock:<8}{data['quantity']:<10}{data['price']:<10}{data['value']:<10}")
    print("-" * 40)
    print(f"Total Investment Value: {total}")
def save_to_txt(summary, total, filename="portfolio_summary.txt"):
    """Saves the summary to a text file."""
    with open(filename, "w") as file:
        file.write("Portfolio Summary:\n")
        file.write(f"{'Stock':<8}{'Quantity':<10}{'Price':<10}{'Value':<10}\n")
        file.write("-" * 40 + "\n")
        for stock, data in summary.items():
            file.write(f"{stock:<8}{data['quantity']:<10}{data['price']:<10}{data['value']:<10}\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total Investment Value: {total}\n")
    print(f"Summary saved to {filename}")
def save_to_csv(summary, total, filename="portfolio_summary.csv"):
    """Saves the summary to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, data in summary.items():
            writer.writerow([stock, data['quantity'], data['price'], data['value']])
        writer.writerow([])
        writer.writerow(["Total", "", "", total])
    print(f"Summary saved to {filename}")
def main():
    # Hardcoded stock prices dictionary
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 136,
        "MSFT": 330,
        "AMZN": 140
    } 
    portfolio = get_portfolio()
    summary, total = calculate_investment(portfolio, stock_prices)
    display_summary(summary, total)
    save_choice = input("Save summary to file? (txt/csv/none): ").lower().strip()
    if save_choice == "txt":
        save_to_txt(summary, total)
    elif save_choice == "csv":
        save_to_csv(summary, total)
    else:
        print("Summary not saved to a file.")
if __name__ == "__main__":
    main()
