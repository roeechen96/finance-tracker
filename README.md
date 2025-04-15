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

1. Clone this repository:

```bash
git clone https://github.com/yourusername/finance-tracker.git
cd finance-tracker
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

To run the test suite using `pytest`:

```bash
pytest
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

## ✅ To-Do

- [ ] Monthly summary report
- [ ] Export PDF reports
- [ ] GUI version

## 🧑‍💻 Contributing

Pull requests are welcome! Feel free to open issues or suggest features.

## 📄 License

This project is licensed under the MIT License.
