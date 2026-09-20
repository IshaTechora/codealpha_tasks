# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("Available Stocks:")
print("AAPL - $180")
print("TSLA - $250")
print("GOOGL - $150")
print("MSFT - $420")
print("AMZN - $190")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment = total_investment + investment

        print("Investment for", stock, ":", investment)
    else:
        print("Stock not available.")

print("\nTotal Investment Value: $", total_investment)
print("Thank you for using Stock Portfolio Tracker!")