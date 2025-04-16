import csv
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from data_entry import get_amount, get_category, get_date, get_description
from pandas import DataFrame


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls) -> None:
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(
        cls, date: str, amount: float, category: str, description: str
    ) -> None:
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        try:
            with open(cls.CSV_FILE, "a", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
                writer.writerow(new_entry)
            print("Entry added successfully")
        except Exception as e:
            print(f"Failed to add entry: {e}")

    @classmethod
    def get_transactions(cls, start_date: str, end_date: str) -> DataFrame:
        try:
            df = pd.read_csv(cls.CSV_FILE)
            df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
            start_date = datetime.strptime(start_date, CSV.FORMAT)
            end_date = datetime.strptime(end_date, CSV.FORMAT)

            if start_date > end_date:
                print("Error: Start date cannot be after end date.")
                return pd.DataFrame()

            mask = (df["date"] >= start_date) & (df["date"] <= end_date)
            filtered_df = df.loc[mask]

            if filtered_df.empty:
                print("No transactions found in the given date range.")
            else:
                print(
                    f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
                )
                print(
                    filtered_df.to_string(
                        index=False,
                        formatters={"date": lambda x: x.strftime(CSV.FORMAT)},
                    )
                )

                total_income = filtered_df[filtered_df["category"] == "Income"][
                    "amount"
                ].sum()
                total_expense = filtered_df[filtered_df["category"] == "Expense"][
                    "amount"
                ].sum()
                print("\nSummary:")
                print(f"Total Income: ${total_income:.2f}")
                print(f"Total Expense: ${total_expense:.2f}")
                print(f"Net Savings: ${(total_income - total_expense):.2f}")

            return filtered_df
        except FileNotFoundError:
            print("Error: CSV file not found. Please add a transaction first.")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error reading transactions: {e}")
            return pd.DataFrame()


def add() -> None:
    CSV.initialize_csv()
    try:
        date = get_date(
            "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
            allow_default=True,
        )
        amount = get_amount()
        category = get_category()
        description = get_description()
        CSV.add_entry(date, amount, category, description)
    except Exception as e:
        print(f"An error occurred while adding transaction: {e}")


def plot_transactions(df: DataFrame) -> None:
    try:
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date")

        # Resample to daily frequency and fill missing days
        daily = (
            df.groupby("category")["amount"]
            .resample("D")
            .sum()
            .unstack(level=0)
            .fillna(0)
        )

        plt.figure(figsize=(10, 5))
        if "Income" in daily:
            plt.plot(daily.index, daily["Income"], label="Income")
        if "Expense" in daily:
            plt.plot(daily.index, daily["Expense"], label="Expense")

        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.title("Income and Expenses Over Time")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Failed to plot transactions: {e}")


def main() -> None:
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if (
                not df.empty
                and input("Do you want to see a plot? (y/n) ").lower() == "y"
            ):
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
