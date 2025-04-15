# Personal Finance Tracker

A simple command-line Python application to help you track your income and expenses using a CSV file and visualize your transactions over time.

## 🚀 Features

- Add new transactions with date, amount, category, and description
- View all transactions within a selected date range
- Get income/expense summaries and net savings
- Generate time-series plots of income vs. expenses
- Fully testable with `pytest`

## 🧰 Technologies Used

- Python 3.8+
- pandas
- matplotlib
- pytest

## 📦 Setup

Clone this repository:

```bash
git clone https://github.com/roeechen96/finance-tracker.git
cd finance-tracker
```

## 🖥️ Usage

Run the main program:

```bash
python main.py
```

Follow the prompts to:
- Add a new transaction
- View and analyze transaction summaries
- Plot daily income vs. expense trends

## 📝 Data Format

All transactions are stored in `finance_data.csv` with the following fields:

| date       | amount | category | description |
|------------|--------|----------|-------------|
| 15-04-2025 | 200.0  | Income   | Freelance    |


