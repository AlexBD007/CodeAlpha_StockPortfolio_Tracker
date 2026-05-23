import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 330,
    "GOOGL": 140,
}

portfolio = {}

print("Stock Portfolio Tracker")
print("Created by Bhushan Dongarwar")
print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(stock, "-", price)

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").strip().upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available.")
        continue

    quantity_input = input("Enter quantity: ").strip()

    if not quantity_input.isdigit():
        print("Please enter a valid quantity.")
        continue

    quantity = int(quantity_input)

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

total_investment = 0

print("\nYour Portfolio")
if not portfolio:
    print("No stocks entered.")
else:
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment
        print(stock, "- Quantity:", quantity, "| Price:", price, "| Total:", investment)

print("\nTotal Investment:", total_investment)

save_option = input("\nDo you want to save this to a file? (yes/no): ").strip().lower()

if save_option in ["yes", "y"]:
    file_type = input("Enter file type (txt/csv): ").strip().lower()

    if file_type == "txt":
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Tracker\n")
            file.write("Created by Bhushan Dongarwar\n\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                file.write(
                    f"{stock} - Quantity: {quantity}, Price: {price}, Total: {investment}\n"
                )
            file.write(f"\nTotal Investment: {total_investment}\n")
        print("Saved in portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Total"])
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                writer.writerow([stock, quantity, price, investment])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])
        print("Saved in portfolio.csv")

    else:
        print("Invalid file type.")
