# Stock Portfolio Tracker

This is my Python project for tracking stock investment using fixed stock prices.

Created by Bhushan Dongarwar.

## About the project

This program takes stock names and quantities from the user, calculates the total investment value, and can save the result in a text file or CSV file.

## Features

- User can enter stock names and quantities
- Uses a dictionary to store stock prices
- Calculates total investment
- Saves output in `portfolio.txt` or `portfolio.csv`

## Stock prices used

- AAPL = 180
- TSLA = 250
- MSFT = 330
- GOOGL = 140

## Concepts used

- Dictionary
- Input and output
- Basic arithmetic
- File handling

## How to run

```bash
python stock_portfolio_tracker.py
```

## Example input

```text
Enter stock name (or 'done' to finish): AAPL
Enter quantity: 2
Enter stock name (or 'done' to finish): TSLA
Enter quantity: 1
Enter stock name (or 'done' to finish): done
```

## Output

The program shows each stock, quantity, price, total value, and final total investment.
