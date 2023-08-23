import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def generate_report(csv_file, period=None):
    # Read the CSV file, skipping the first 9 lines
    df = pd.read_csv(csv_file, skiprows=9)

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
