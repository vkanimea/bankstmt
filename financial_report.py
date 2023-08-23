import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def generate_report(csv_file, period=None):
    # Read the first 15 lines of the file
    with open(csv_file, 'r') as f:
        lines = [next(f) for x in range(15)]

    # Find the line that contains the headers
    header_line = next((i for i, line in enumerate(lines) if 'date' in line and 'description' in line and 'debit' in line and 'credit' in line and 'balance' in line), None)

    if header_line is None:
        raise Exception("The CSV file does not contain a header line with 'date', 'description', 'debit', 'credit', and 'balance' in the first 15 lines.")

    # Read the CSV file, skipping the lines before the header
    df = pd.read_csv(csv_file, skiprows=header_line)

    # Convert the date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Filter the data based on the specified period
    if period == 'w':
        df = df[df['date'] >= datetime.now() - pd.DateOffset(weeks=1)]
    elif period == 'm':
        df = df[df['date'] >= datetime.now() - pd.DateOffset(months=1)]
    elif period == 'q':
        df = df[df['date'] >= datetime.now() - pd.DateOffset(months=3)]

    # Separate expenses and income
    expenses = df[df['debit'].notna()]
    income = df[df['credit'].notna()]

    # Generate summary tables
    expenses_summary = expenses.groupby('description').sum()
    income_summary = income.groupby('description').sum()

    # Generate pie charts
    expenses_summary['debit'].plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expenses')
    plt.show()

    income_summary['credit'].plot(kind='pie', autopct='%1.1f%%')
    plt.title('Income')
    plt.show()

    # Generate bar graphs
    expenses_summary['debit'].plot(kind='bar')
    plt.title('Expenses')
    plt.show()

    income_summary['credit'].plot(kind='bar')
    plt.title('Income')
    plt.show()

# Call the function with your CSV file
generate_report('your_file.csv')
